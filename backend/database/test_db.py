from sqlalchemy.orm import Session

from connection import engine
from models import Customer, Product, Sale


session = Session(bind=engine)


customers = session.query(Customer).all()

print("\nCUSTOMERS")
print("----------------")

for customer in customers:
    print(customer.id, customer.name, customer.region)


products = session.query(Product).all()

print("\nPRODUCTS")
print("----------------")

for product in products:
    print(product.id, product.name, product.category, product.price)


sales = session.query(Sale).all()

print("\nSALES")
print("----------------")

for sale in sales:
    print(
        sale.id,
        sale.customer_id,
        sale.product_id,
        sale.quantity,
        sale.total_amount,
        sale.sale_date
    )


session.close()