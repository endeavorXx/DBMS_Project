import mysql.connector

class connectDatabase:

    ## use your own sql credentials to login to your database
    def __init__(self):
        self._host = "localhost"
        self._port = 3306
        self._user = "root"
        self._password = "123456"
        self._auth_plugin = "mysql_native_password"
        self.con = None
        self.cursor = None

    def connect_db(self):

        self.con = mysql.connector.connect(
            host = self._host,
            user = self._user,
            password = self._password,
            auth_plugin = self._auth_plugin
        )
        self.cursor = self.con.cursor(dictionary = True)
        self.cursor.execute("use megamarket;")

    def get_customer_authentication(self, phone_no, password):
        self.connect_db()
        condition = f"phone_no = '{phone_no}' and password = '{password}'"
        sql = f"""
                select customer_id,first_name,last_name,phone_no,street,city,state,pin_code from customer where {condition};
            """ 
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    def add_customer_info(self, first_name, last_name, phone_no, street, city, state, pin_code, pswd):
        self.connect_db()

        sql = f"""
            INSERT INTO customer (first_name, last_name, phone_no, street, city, state, pin_code, password)
VALUES('{first_name}','{last_name}','{phone_no}','{street}','{city}','{state}',{pin_code},'{pswd}')
        """
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def update_customer_info(self, customer_id, first_name, last_name, phone_no, street, city, state, pin_code):
        self.connect_db()

        sql = f"""
            UPDATE CUSTOMER SET first_name = '{first_name}',last_name = '{last_name}', phone_no = '{phone_no}', street = '{street}', city = '{city}', state = '{state}', pin_code = {int(pin_code)}
            where customer_id = {customer_id};
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def search_customer_info(self, customer_id = None, first_name = None, last_name = None, phone_no = None, street = None, city = None, state = None, pin_code = None):
        self.connect_db()

        condition = ""

        if customer_id:
            ## customer_id is an integer in our tables
            condition += f"customer_id = {customer_id}"
        else:
            if first_name:
                if condition:
                    condition += f"and first_name LIKE '%{first_name}%'"
                else:
                    condition += f"first_name LIKE '%{first_name}%'"
            if last_name:
                if condition:
                    condition += f"and last_name LIKE '%{last_name}%'"
                else:
                    condition += f"last_name LIKE '%{last_name}%'"
            if phone_no:
                if condition:
                    condition += f"and phone_no = '{phone_no}'"
                else:
                    condition += f"phone_no = '{phone_no}'"
            if street:
                if condition:
                    condition += f"and street = '{street}'"
                else:
                    condition += f"street = '{street}'"
            if state:
                if condition:
                    condition += f"and state = '{state}'"
                else:
                    condition += f"state = '{state}'"
            if city:
                if condition:
                    condition += f"and city = '{city}'"
                else:
                    condition += f"city = '{city}'"
            if pin_code:
                if condition:
                    condition += f"and pin_code LIKE '%{pin_code}%'"
                else:
                    condition += f"pin_code LIKE '%{pin_code}%'"

            
        if condition:
            sql = f"""
                select customer_id,first_name,last_name,phone_no,street,city,state,pin_code from customer where {condition};
            """ 
        else:
            sql = f"""
                select customer_id,first_name,last_name,phone_no,street,city,state,pin_code from customer;
            """ 
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    def search_order_info(self,order_id = None,customer_id = None,transaction_id = None):
        self.connect_db()
        condition = ""

        if customer_id:
            condition += f"customer_id = {customer_id}"
        else:
            if transaction_id:
                if condition:
                    condition += f"and transaction_id = '{transaction_id}'"
                else:
                    condition += f"transaction_id = '{transaction_id}'"
            else:
                if order_id:
                    if condition:
                        condition += f"and order_id = {order_id}"
                    else:
                        condition += f"order_id = {order_id}"
        if condition:
            sql = f"""
                SELECT * FROM orders where {condition}
            """ 
        else:
            sql = f"""
                SELECT * FROM orders
            """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        finally:
            self.con.close()

    def add_order_info(self, customer_id, payment_method, amt, transaction_id, order_date, order_time, delivery_agent_id , delivery_date, delivery_status):
        self.connect_db()
        
        sql = f"""
            INSERT INTO orders (customer_id, payment_method, amount, transaction_id, order_date, order_time, delivery_agent_id, delivery_date, delivery_status)
            VALUES({customer_id},'{payment_method}','{amt}','{transaction_id}','{order_date}','{order_time}','{delivery_agent_id}','{delivery_date}','{delivery_status}');
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    

    def add_order_details_info(self, order_id, product_id, qty, cost_per_piece, total):
        self.connect_db()
        
        sql = f"""
            INSERT INTO order_details (order_id, product_id, quantity, cost_per_piece, total)
            VALUES({order_id},'{product_id}','{qty}','{cost_per_piece}','{total}');
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()
    
    def search_product_info_All(self, product_id = None, product_name = None, product_category = None, product_price = None, product_rating = None, product_qty = None, product_desc = None, image_url = None):
        self.connect_db()

        condition = ""

        if product_id:
            ## customer_id is an integer in our tables
            condition += f"product_id = {product_id}"
        else:
            if product_name:
                if condition:
                    condition += f"and name LIKE '%{product_name}%'"
                else:
                    condition += f"name LIKE '%{product_name}%'"
            if product_category:
                if condition:
                    condition += f"and category LIKE '%{product_category}%'"
                else:
                    condition += f"category LIKE '%{product_category}%'"
            if product_price:
                if condition:
                    condition += f"and price = '{product_price}'"
                else:
                    condition += f"price = '{product_price}'"
            if product_rating:
                if condition:
                    condition += f"and rating = '{product_rating}'"
                else:
                    condition += f"rating = '{product_rating}'"
            if  product_qty:
                if condition:
                    condition += f"and qty = '{product_qty}'"
                else:
                    condition += f"qty = '{product_qty}'"
            if product_desc:
                if condition:
                    condition += f"and description = '{product_desc}'"
                else:
                    condition += f"description = '{product_desc}'"

            
        if condition:
            sql = f"""
                select * from product where {condition};
            """ 
        else:
            sql = f"""
                select * from product;
            """ 
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        finally:
            self.con.close()
    
    def get_all_product(self):
        try:
            self.connect_db()
            
            self.cursor.execute("START TRANSACTION")
            
            sql = "SELECT * FROM product"
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            
            self.con.commit()
            
            return result
            
        except Exception as e:
            self.con.rollback()
            return e
            
        finally:
            self.con.close()


    def add_product_info(self, name, category, price, rating, qty, description = None, url = None):
        self.connect_db()

        sql = f"""
            INSERT INTO product (name, category, price, rating, qty, description, url)
VALUES('{name}','{category}',{price},{rating},{qty},'{description}','{url}');
        """
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def update_product_info(self, product_id, name, category, price, qty, rating, description, url):
        self.connect_db()
        if url == "":
            sql = f"""
                UPDATE product SET name = '{name}',category = '{category}', price = {price}, rating = {rating}, qty = {qty}, description = '{description}'
                where product_id = {product_id};
            """
        else:
            sql = f"""
                UPDATE product SET name = '{name}',category = '{category}', price = {price}, rating = {rating}, qty = {qty}, description = '{description}', url = '{url}'
                where product_id = {product_id};
            """

        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()
    
    def add_order(self,customer_id,payment_method, amount, transaction_id, order_date, order_time, delivery_date,delivery_status = "Pending"):
        self.connect_db()

        sql = f"""
            INSERT INTO orders (customer_id, payment_method, amount, transaction_id, order_date, order_time, delivery_date, delivery_status)
VALUES({customer_id},'{payment_method}',{amount},'{transaction_id}','{order_date}','{order_time}','{delivery_date}','{delivery_status}');
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def get_AllCart_info(self):
        self.connect_db()
        sql = f"""
            SELECT * from cart;
        """
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def clearCart(self, customer_id):
        self.connect_db()

        sql = f"""
            DELETE FROM cart where customer_id = {customer_id};
        """ 

        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()
    
    def update_cart(self, customer_id,product_id,new_quantity, new_total):
        self.connect_db()

        sql1 = f"""
            UPDATE cart
            SET quantity = {new_quantity}
            WHERE customer_id = {customer_id}
            AND product_id = {product_id};
        """ 

        sql2 = f"""
            UPDATE cart
            SET total = {new_total}
            WHERE customer_id = {customer_id}
            AND product_id = {product_id};
        """
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql1)
            self.cursor.execute(sql2)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def get_cart_info(self, customer_id):
        self.connect_db()
        self.cursor = self.con.cursor(dictionary = False)
        sql = f"""
            SELECT * FROM cart where customer_id = {customer_id};
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.cursor = self.con.cursor(dictionary = True)
            self.con.close()
    
    def add_product_to_cart(self, customer_id, product_id, product_name, price, total, quantity, url):
        self.connect_db()
        length = len(url)
        url_new = ""
        for i in range(length):
            ch = url[i]
            url_new += ch
            if ch == "\\":
                url_new += "\\"
        url = url_new
        sql = f"""
            INSERT INTO cart (customer_id, product_id, product_name, quantity, price, total, url)
VALUES ({customer_id}, {product_id}, '{product_name}', {quantity}, {price}, {total}, '{url}');
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()
    
    def search_product_info(self, product_id):
        self.connect_db()
        self.cursor = self.con.cursor(dictionary = False)
        sql = f"""
            SELECT name,price,url FROM PRODUCT where product_id = {product_id}
        """
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.cursor = self.con.cursor(dictionary = True)
            self.con.close()

    def get_all_customers(self):
        self.connect_db()

        sql = f"""
            SELECT * FROM customer;
        """ 
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    
    def search_vendor_info(self, vendor_id = None, vendor_name = None, street = None, city = None, state = None, phone_no = None):
        self.connect_db()

        condition = ""

        if vendor_id:
            ## customer_id is an integer in our tables
            condition += f"vendor_id = {vendor_id}"
        else:
            if vendor_name:
                if condition:
                    condition += f"and vendor_name LIKE '%{vendor_name}%'"
                else:
                    condition += f"vendor_name LIKE '%{vendor_name}%'"
            if street:
                if condition:
                    condition += f"and street LIKE '%{street}%'"
                else:
                    condition += f"street LIKE '%{street}%'"
            if city:
                if condition:
                    condition += f"and city LIKE '%{city}%'"
                else:
                    condition += f"city LIKE '%{city}%'"
            if  state:
                if condition:
                    condition += f"and state LIKE '%{state}%'"
                else:
                    condition += f"state LIKE '%{state}%'"
            if phone_no:
                if condition:
                    condition += f"and phone_no = '{phone_no}'"
                else:
                    condition += f"phone_no = '{phone_no}'"

            
        if condition:
            sql = f"""
                select * from vendor where {condition};
            """ 
        else:
            sql = f"""
                select * from vendor;
            """ 
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        finally:
            self.con.close()

    def add_vendor_info(self, vendor_name, street, city, state, phone_no):
        self.connect_db()

        sql = f"""
            INSERT INTO vendor (vendor_name, street, city, state, phone_no)
VALUES('{vendor_name}', '{street}', '{city}','{state}','{phone_no}')
        """
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    def update_vendor_info(self, vendor_id, vendor_name, street, city, state, phone_no):
        self.connect_db()

        sql = f"""
            UPDATE vendor SET vendor_name = '{vendor_name}', phone_no = '{phone_no}', street = '{street}', city = '{city}', state = '{state}'
            where vendor_id = {vendor_id};
        """ 
        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()



    def add_supply_info(self, vendor_id, product_id, qty_supplied, date, time, cost_per_piece, total_cost, margin_percentage):
        self.connect_db()
        self.cursor.execute("SELECT CURDATE()")

        # Fetch the result of the query
        # print(self.cursor.fetchall()[0])
        current_date = self.cursor.fetchall()[0]['CURDATE()']
        # print("Current Date:", current_date)

        # Execute a SQL query with CURTIME() to get the current time
        
        self.cursor.execute("SELECT CURTIME()")

        # Fetch the result of the query
        current_time = self.cursor.fetchall()[0]['CURTIME()']
        # print(current_time)
        
        sql = f"""
    INSERT INTO supplies (vendor_id, product_id, qty_supplied, date, time, cost_per_piece, total_cost, margin_percentage)
    VALUES ({vendor_id}, {product_id}, {qty_supplied}, '{current_date}', '{current_time}', {cost_per_piece}, {total_cost}, {margin_percentage})
"""

        try:
            self.cursor.execute("START TRANSACTION")
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            self.con.rollback()
            return E
        finally:
            self.con.close()

    def delete_supply_info(self, supply_id):
        self.connect_db()

        sql = f"""
            DELETE FROM SUPPLIES WHERE SUPPLY_ID = {supply_id}
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        finally:
            self.con.close()

    def search_supply_info(self, supply_id, vendor_id, product_id, date):
        self.connect_db()

        condition = ""

        if supply_id:
            ## customer_id is an integer in our tables
            condition += f"supply_id = {supply_id}"
        else:
            
            if vendor_id:
                if condition:
                    condition += f"and vendor_id = {vendor_id}"
                else:
                    condition += f"vendor_id = {vendor_id}"
            if product_id:
                if condition:
                    condition += f"and product_id = {product_id}"
                else:
                    condition += f"product_id = {product_id}"
            if date:
                if condition:
                    condition += f"and date = {date}"
                else:
                    condition += f"date = {date}"

            
        if condition:
            sql = f"""
                select * from supplies where {condition};
            """ 
        else:
            sql = f"""
                select * from supplies;
            """ 
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        
        finally:
            self.con.close()
        