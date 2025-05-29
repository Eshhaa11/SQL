from sqlmodel import Field, SQLModel, Session, create_engine, select
from typing import Optional

#Define your PostgreSQL connection URL
DATABASE_URL = "postgresql+psycopg2://postgres:3031@localhost/myydb"

#Initialize the database engine
engine = create_engine(DATABASE_URL, echo=True)

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    image: str


def create_db():
    SQLModel.metadata.create_all(engine)

def create_product(name: str, price: float, image: str):
    with Session(engine) as session:
        product = Product(name=name, price=price, image=image)
        session.add(product)
        session.commit()
        session.refresh(product)
        print(f"Created: {product}")

def read_products():
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
        print("All products:")
        for products in products:
            print(products)

def update_products(product_id: int, new_name: str, new_price: float, new_image: str):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if product:
            product.name = new_name
            product.price = new_price
            product.image = new_image
            session.add(product)
            session.commit()
            session.refresh(product)
            print(f"Updated: {product}")
        else:
            print("Product not found")

def delete_product(product_id: int):
    with Session(engine) as session:
        product = session.get(Product, product_id)
        if product:
            session.delete(product)
            session.commit()
            print(f"Deleted product with ID: {product_id}")
        else:
            print("Product not found")


if __name__ == "__main__":
    create_db()


    # Products
    create_product("Laptop", 1200.00, "https://example.com/laptop.jpg")
    create_product("Mouse", 25.99, "https://example.com/mouse.jpg")
    read_products()
    update_products(1, "Gaming Laptop", 1500.00, )
    delete_product(2)
    read_products()

    





