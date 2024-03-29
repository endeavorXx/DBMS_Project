import mysql.connector

class connectDatabase:
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

    def add_customer_info(self, first_name, last_name, phone_no, street, city, state, pswd):
        self.connect_db()

        sql = f"""
            INSERT INTO customer (first_name, last_name, phone_no, street, city, state, password)
            VALUES('{first_name}','{last_name}','{phone_no}','{street}','{city}','{state}','{pswd}');
        """
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    def add_order_info(self, customer_id, payment_method, amt, transaction_id, order_date, order_time, delivery_agent_id , delivery_date, delivery_status):
        self.connect_db()

        sql = f"""
            INSERT INTO orders (customer_id, payment_method, amount, transaction_id, order_date, order_time, delivery_agent_id, delivery_date, delivery_status)
            VALUES({customer_id},'{payment_method}','{amt}','{transaction_id}','{order_date}','{order_time}','{delivery_agent_id}','{delivery_date}','{delivery_status}');
        """ 
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    def search_order_info(self,transaction_id):
        self.connect_db()

        sql = f"""
            SELECT * FROM orders where transaction_id = '{transaction_id}'
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

    def add_order_details_info(self, order_id, product_id, qty, cost_per_piece, total):
        self.connect_db()

        sql = f"""
            INSERT INTO order_details (order_id, product_id, quantity, cost_per_piece, total)
            VALUES({order_id},'{product_id}','{qty}','{cost_per_piece}','{total}');
        """ 
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()

    def update_customer_info(self, customer_id, first_name, last_name, phone_no, street, city, state, pswd):
        self.connect_db()

        sql = f"""
            UPDATE CUSTOMER SET firstname = '{first_name}',lastname = '{last_name}', phone_no = '{phone_no}', street = '{street}', city = '{city}', state = '{state}', password = '{pswd}'
            where customer_id = {customer_id};
        """ 
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:

            self.con.rollback()
            return E
        finally:
            self.con.close()
    
    def get_all_product(self):
        self.connect_db()

        sql = f"""
            SELECT * FROM PRODUCT
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
    
    def add_order(self,customer_id,payment_method, amount, transaction_id, order_date, order_time, delivery_date,delivery_status = "Pending"):
        self.connect_db()

        sql = f"""
            INSERT INTO orders (customer_id, payment_method, amount, transaction_id, order_date, order_time, delivery_date, delivery_status)
VALUES({customer_id},'{payment_method}',{amount},'{transaction_id}','{order_date}','{order_time}','{delivery_date}','{delivery_status}');
        """ 
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as E:
            print("Query not executed")
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
    