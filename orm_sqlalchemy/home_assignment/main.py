from datetime import datetime
import os
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

db_filename = 'db.db'
if os.path.exists(db_filename):
    os.remove(db_filename)

engine = create_engine(f"sqlite:///{db_filename}")

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Customer(Base):
    __tablename__ = "customers"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String)
    email = Column("email", String, unique=True)
    orders = relationship("Order", back_populates="customer")

    def __repr__(self):
        return f"<{self.name}>"


class Product(Base):
    __tablename__ = "products"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String, unique=True)
    price = Column("price", Float)
    orders = relationship("Order", secondary="order_products", back_populates="products")


class Order(Base):
    __tablename__ = "orders"

    id = Column("id", Integer, primary_key=True)
    order_datetime = Column("order_datetime", DateTime)
    customer_id = Column("customer_id", Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="orders")
    products = relationship("Product", secondary="order_products", back_populates="orders")

    def __repr__(self):
        return f"<{self.id} - {self.order_datetime}>"


class OrderProduct(Base):
    __tablename__ = "order_products"

    order_id = Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True)
    product_id = Column(
        "product_id", Integer, ForeignKey("products.id"), primary_key=True
    )
    quantity = Column("quantity", Integer)


Base.metadata.create_all(bind=engine)


customer_1 = Customer(name="customer 1", email="customer_1@mail.com")
customer_2 = Customer(name="customer 2", email="customer_2@mail.com")
customer_3 = Customer(name="customer 3", email="customer_3@mail.com")

customer_list = [customer_1, customer_2, customer_3]
session.add_all(customer_list)

product_1 = Product(name="product 1", price=1.1)
product_2 = Product(name="product 2", price=2.2)
product_3 = Product(name="product 3", price=3.3)
product_4 = Product(name="product 4", price=4.4)
product_5 = Product(name="product 5", price=5.5)

product_list = [product_1, product_2, product_3, product_4, product_5]
session.add_all(product_list)

db_customer_1 = session.query(Customer).filter_by(email=customer_1.email).first()
order_1 = Order(order_datetime=datetime.now(), customer_id=db_customer_1.id)
order_2 = Order(order_datetime=datetime.now(), customer_id=db_customer_1.id)

db_customer_2 = session.query(Customer).filter_by(email=customer_2.email).first()
# db_customer_2 = session.query(Customer).filter(Customer.email == customer_2.email).first()
order_3 = Order(order_datetime=datetime.now(), customer_id=db_customer_2.id)

order_list = [order_1, order_2, order_3]
session.add_all(order_list)

db_order_1 = session.get(Order, 1)
db_product_1 = session.get(Product, 1)
order_products_1 = OrderProduct(
    order_id=db_order_1.id, product_id=db_product_1.id, quantity=3
)

session.add(order_products_1)

session.commit()

# witouth 
# db_customer = session.query(Customer).filter_by(email=customer_1.email).first()
# db_customer_orders = session.query(Order).filter_by(customer_id=db_customer.id).all()
# print(db_customer_orders)
# for customer_order in db_customer_orders:
#     print(customer_order.order_datetime)

db_customer = session.query(Customer).filter_by(email=customer_1.email).first()
print(db_customer.orders)
for order in db_customer.orders:
    print(order)


# db_customers = session.query(Customer).all()
# for customer in db_customers:
#     print(f"- {customer}")
#     db_customer_orders = session.query(Order).filter_by(customer_id=customer.id).all()
#     for customer_order in db_customer_orders:
#         print(f"    - {customer_order}")

db_customer_list = session.query(Customer).all()
for customer in db_customer_list:
    print(f"- {customer}")
    for customer_order in customer.orders:
        print(f"    - {customer_order}")

db_order_list = session.query(Order).all()
for order in db_order_list:
    print(order.products)

db_product_list = session.query(Product).all()
for product in db_product_list:
    print(product.orders)