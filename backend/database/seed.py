from sqlalchemy.orm import Session

from connection import engine
from models import Customer, Product, Sale


def seed_database():
    session = Session(bind=engine)

    # Clear existing data
    session.query(Sale).delete()
    session.query(Product).delete()
    session.query(Customer).delete()

    # -------------------------
    # Customers
    # -------------------------

    customers = [
        Customer(name="Rahul Sharma", region="South"),
        Customer(name="Priya Reddy", region="South"),
        Customer(name="Arjun Mehta", region="West"),
        Customer(name="Sneha Patel", region="West"),
        Customer(name="Vikram Singh", region="North"),
        Customer(name="Ananya Gupta", region="North"),
        Customer(name="Karthik Rao", region="South"),
        Customer(name="Neha Kapoor", region="North"),
        Customer(name="Rohan Das", region="East"),
        Customer(name="Meera Iyer", region="South"),
    ]

    session.add_all(customers)
    session.commit()

    # -------------------------
    # Products
    # -------------------------

    products = [
        Product(
            name="Laptop",
            category="Electronics",
            price=65000
        ),
        Product(
            name="Smartphone",
            category="Electronics",
            price=35000
        ),
        Product(
            name="Monitor",
            category="Electronics",
            price=18000
        ),
        Product(
            name="Keyboard",
            category="Accessories",
            price=2500
        ),
        Product(
            name="Mouse",
            category="Accessories",
            price=1500
        ),
        Product(
            name="Headphones",
            category="Accessories",
            price=5000
        ),
        Product(
            name="Tablet",
            category="Electronics",
            price=28000
        ),
        Product(
            name="Smartwatch",
            category="Wearables",
            price=12000
        ),
        Product(
            name="Webcam",
            category="Accessories",
            price=4500
        ),
        Product(
            name="Printer",
            category="Office",
            price=15000
        ),
    ]

    session.add_all(products)
    session.commit()

    # -------------------------
    # Sales
    # -------------------------

    sales = [
        Sale(
            customer_id=1,
            product_id=1,
            quantity=1,
            total_amount=65000,
            sale_date="2026-01-05"
        ),
        Sale(
            customer_id=2,
            product_id=2,
            quantity=2,
            total_amount=70000,
            sale_date="2026-01-08"
        ),
        Sale(
            customer_id=3,
            product_id=3,
            quantity=1,
            total_amount=18000,
            sale_date="2026-01-12"
        ),
        Sale(
            customer_id=4,
            product_id=4,
            quantity=3,
            total_amount=7500,
            sale_date="2026-01-15"
        ),
        Sale(
            customer_id=5,
            product_id=5,
            quantity=2,
            total_amount=3000,
            sale_date="2026-01-20"
        ),
        Sale(
            customer_id=6,
            product_id=6,
            quantity=2,
            total_amount=10000,
            sale_date="2026-01-25"
        ),
        Sale(
            customer_id=7,
            product_id=7,
            quantity=1,
            total_amount=28000,
            sale_date="2026-02-02"
        ),
        Sale(
            customer_id=8,
            product_id=8,
            quantity=2,
            total_amount=24000,
            sale_date="2026-02-07"
        ),
        Sale(
            customer_id=9,
            product_id=9,
            quantity=3,
            total_amount=13500,
            sale_date="2026-02-11"
        ),
        Sale(
            customer_id=10,
            product_id=10,
            quantity=1,
            total_amount=15000,
            sale_date="2026-02-15"
        ),
        Sale(
            customer_id=1,
            product_id=2,
            quantity=1,
            total_amount=35000,
            sale_date="2026-02-20"
        ),
        Sale(
            customer_id=2,
            product_id=1,
            quantity=1,
            total_amount=65000,
            sale_date="2026-02-25"
        ),
        Sale(
            customer_id=3,
            product_id=6,
            quantity=1,
            total_amount=5000,
            sale_date="2026-03-01"
        ),
        Sale(
            customer_id=4,
            product_id=7,
            quantity=2,
            total_amount=56000,
            sale_date="2026-03-05"
        ),
        Sale(
            customer_id=5,
            product_id=3,
            quantity=2,
            total_amount=36000,
            sale_date="2026-03-10"
        ),
        Sale(
            customer_id=6,
            product_id=4,
            quantity=2,
            total_amount=5000,
            sale_date="2026-03-15"
        ),
        Sale(
            customer_id=7,
            product_id=5,
            quantity=4,
            total_amount=6000,
            sale_date="2026-03-20"
        ),
        Sale(
            customer_id=8,
            product_id=1,
            quantity=1,
            total_amount=65000,
            sale_date="2026-03-25"
        ),
        Sale(
            customer_id=9,
            product_id=8,
            quantity=1,
            total_amount=12000,
            sale_date="2026-04-01"
        ),
        Sale(
            customer_id=10,
            product_id=2,
            quantity=2,
            total_amount=70000,
            sale_date="2026-04-05"
        ),
        Sale(
            customer_id=1,
            product_id=3,
            quantity=2,
            total_amount=36000,
            sale_date="2026-04-10"
        ),
        Sale(
            customer_id=2,
            product_id=6,
            quantity=3,
            total_amount=15000,
            sale_date="2026-04-15"
        ),
        Sale(
            customer_id=3,
            product_id=10,
            quantity=1,
            total_amount=15000,
            sale_date="2026-04-20"
        ),
        Sale(
            customer_id=4,
            product_id=9,
            quantity=2,
            total_amount=9000,
            sale_date="2026-04-25"
        ),
        Sale(
            customer_id=5,
            product_id=7,
            quantity=1,
            total_amount=28000,
            sale_date="2026-05-01"
        ),
        Sale(
            customer_id=6,
            product_id=8,
            quantity=2,
            total_amount=24000,
            sale_date="2026-05-05"
        ),
        Sale(
            customer_id=7,
            product_id=1,
            quantity=1,
            total_amount=65000,
            sale_date="2026-05-10"
        ),
        Sale(
            customer_id=8,
            product_id=2,
            quantity=1,
            total_amount=35000,
            sale_date="2026-05-15"
        ),
        Sale(
            customer_id=9,
            product_id=4,
            quantity=4,
            total_amount=10000,
            sale_date="2026-05-20"
        ),
        Sale(
            customer_id=10,
            product_id=5,
            quantity=3,
            total_amount=4500,
            sale_date="2026-05-25"
        ),
    ]

    session.add_all(sales)
    session.commit()

    print("Database seeded successfully!")
    print("10 customers added.")
    print("10 products added.")
    print("30 sales added.")

    session.close()


if __name__ == "__main__":
    seed_database()