create table customer
(
    customer_id int         not null
        primary key,
    first_name  varchar(50) not null,
    last_name   varchar(50) not null,
    phone_no    varchar(20) null,
    street      varchar(50) not null,
    city        varchar(50) not null,
    state       varchar(50) not null,
    password    varchar(20) not null
);

create table demo
(
    id   int          null,
    name varchar(250) null
);

create table employee
(
    employee_id int         not null
        primary key,
    first_name  varchar(50) not null,
    last_name   varchar(50) not null,
    designation varchar(50) not null,
    start_date  varchar(20) not null,
    salary      int         not null,
    phone_no    varchar(20) null,
    password    varchar(20) not null
);

create table orders
(
    order_id          int         not null
        primary key,
    customer_id       int         not null,
    payment_method    varchar(50) not null,
    amount            double      not null,
    transaction_id    int         not null,
    order_date        varchar(50) not null,
    order_time        varchar(50) not null,
    delivery_agent_id int         not null,
    delivery_date     varchar(50) not null,
    delivery_status   varchar(50) not null,
    constraint orders_ibfk_1
        foreign key (customer_id) references customer (customer_id),
    constraint orders_ibfk_2
        foreign key (delivery_agent_id) references employee (employee_id)
);

create index customer_id
    on orders (customer_id);

create index delivery_agent_id
    on orders (delivery_agent_id);

create table product
(
    product_id  int          not null
        primary key,
    name        varchar(50)  not null,
    category    varchar(100) not null,
    price       int          not null,
    rating      int          not null,
    qty         int          not null,
    description varchar(100) null,
    check (`price` >= 0),
    check ((`rating` <= 5) and (`rating` >= 1)),
    check (`qty` >= 0)
);

create table order_details
(
    order_id       int    not null,
    product_id     int    not null,
    quantity       double not null,
    cost_per_piece double null,
    total          double not null,
    constraint order_details_ibfk_1
        foreign key (order_id) references orders (order_id),
    constraint order_details_ibfk_2
        foreign key (product_id) references product (product_id),
    check (`cost_per_piece` >= 0)
);

create index order_id
    on order_details (order_id);

create index product_id
    on order_details (product_id);

create table vendor
(
    vendor_id   int          not null
        primary key,
    vendor_name varchar(100) null,
    street      varchar(100) not null,
    city        varchar(50)  not null,
    state       varchar(50)  not null,
    phone_no    varchar(20)  null
);

create table supplies
(
    vendor_id    int         not null,
    product_id   int         not null,
    employee_id  int         not null,
    qty_supplied int         not null,
    date         varchar(50) not null,
    cost         double      not null,
    total_cost   double      not null,
    constraint supplies_ibfk_1
        foreign key (vendor_id) references vendor (vendor_id),
    constraint supplies_ibfk_2
        foreign key (employee_id) references employee (employee_id),
    constraint supplies_ibfk_3
        foreign key (product_id) references product (product_id)
);

create index employee_id
    on supplies (employee_id);

create index product_id
    on supplies (product_id);

create index vendor_id
    on supplies (vendor_id);


