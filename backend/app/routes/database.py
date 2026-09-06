from fastapi import APIRouter
from sqlalchemy.orm import Session

from database.connection import engine
from database.models import Customer, Product, Sale


router = APIRouter()


@router.get("/customers")
def get_customers():
    session = Session(bind=engine)

    customers = session.query(Customer).all()

    result = []

    for customer in customers:
        result.append({
            "id": customer.id,
            "name": customer.name,
            "region": customer.region
        })

    session.close()

    return result


@router.get("/products")
def get_products():
    session = Session(bind=engine)

    products = session.query(Product).all()

    result = []

    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price
        })
@router.get("/sales")
def get_sales():
    session = Session(bind=engine)

    sales = session.query(Sale).all()

    result = []

    for sale in sales:
        result.append({
            "id": sale.id,
            "customer_id": sale.customer_id,
            "product_id": sale.product_id,
            "quantity": sale.quantity,
            "total_amount": sale.total_amount,
            "sale_date": sale.sale_date
        })
    session.close()

    return result