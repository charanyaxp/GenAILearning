"""This module will have mcp server to generate sales data
"""

from typing import Literal
from mcp.server.fastmcp import FastMCP
from utils import get_database_connection

mcp = FastMCP("data-generator")

@mcp.tool()
def create_user(
        username: str,
        password: str,
        email: str,
        firstname: str,
        lastname: str,
        address: str,
        city: str,
        state: str,
        zip: int,
        country: str) -> Literal["Success", "Failed"]:
    #INSERT INTO users (username, password_hash, email, first_name, last_name, address, city, state, zip_code, country) VALUES
    #('john_doe', 'hashed_password_1', 'john.doe@example.com', 'John', 'Doe', '123 Main St', 'Anytown', 'CA', '90210', 'USA')
    """
    Adds a new user to the database with his name, address and contact address

    Returns:
    Str: Success if record added successfully otherwise Failed 
    """
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        insert_user_sql = f"INSERT INTO users (username, password_hash, email, first_name, last_name, address, city, state, zip_code, country) VALUES ('{username}', '{password}', '{email}', '{firstname}', '{lastname}', '{address}', '{city}', '{state}', '{zip}', '{country}')"
        cursor.execute(insert_user_sql)
        connection.commit()
    except Exception:
        return "Failed"
    return "Success"
    

@mcp.tool()
def create_product(
        name: str,
        description: str,
        price: float,
        stock_quantity: int,
        category_id: int = 1,
        image_url: str = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Image_not_available.png/640px-Image_not_available.png") -> Literal["Success", "Failed"]:
    """Creates  a product

    Returns:
        str: Success if saved false otherwise
    """
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        insert_product_sql = f"INSERT INTO products (name, description, price, stock_quantity, category_id, image_url) VALUES ('{name}', '{description}', {price}, {stock_quantity}, {category_id}, '{image_url}')"
        cursor.execute(insert_product_sql)
        connection.commit()
    except Exception:
        return "Failed"
    return "Success"


@mcp.tool()
def create_category(name: str, desc: str) -> Literal["Success","Failed"]:
    """Creates a new category

    Returns:
        str: Success if saved false otherwise
    """
    try:
        connection = get_database_connection()
        cursor = connection.cursor()
        create_category_sql = f"INSERT INTO categories (name, description) VALUES ('{name}', '{desc}')"
        cursor.execute(create_category_sql)
        connection.commit()
    except Exception:
        return "Failed"
    return "Success"


@mcp.tool()
def get_products_list() -> list:
    """This method gets the latest product
    """
    connection = get_database_connection()
    cursor = connection.cursor()
    latest_product_sql = 'SELECT * FROM `products`'
    cursor.execute(latest_product_sql)
    products = cursor.fetchall()
    message = []
    for product in products:
        fstr = f"{product[0]}. {product[1]}"
        message.append(fstr)
    return message
    

@mcp.resource(uri="products://latest")
def get_products():
    """This method gets the latest product
    """
    connection = get_database_connection()
    cursor = connection.cursor()
    latest_product_sql = 'SELECT * FROM `products` ORDER BY product_id DESC LIMIT 1;'
    cursor.execute(latest_product_sql)
    products = cursor.fetchall()
    product = products[0]
    message = f"{product[1]}, {product[2]}"
    return message


@mcp.resource(uri="product://selected/{product_id}")
def get_selected_product(product_id: int):
    """This method gets the selected product
    """
    connection = get_database_connection()
    cursor = connection.cursor()
    latest_product_sql = f"SELECT * FROM `products` Where product_id = {product_id};"
    cursor.execute(latest_product_sql)
    products = cursor.fetchall()
    product = products[0]
    message = f"{product[1]} => {product[2]}"
    return message


@mcp.resource(uri="categories://{name}")
def get_category_by_name(name:str):
    """Get the category by name
    """
    connection = get_database_connection()
    cursor = connection.cursor()
    latest_product_sql = f"SELECT * FROM `categories` WHERE name LIKE '%{name}%';"
    cursor.execute(latest_product_sql)
    categories = cursor.fetchall()
    message = ""
    for category in categories:
        message = f"id => {category[0]} \n name => {category[1]}"
    return message


# @mcp.resource(uri="users://latest")
# def get_users():
#     pass


# @mcp.resource(uri="categories://latest")
# def get_categories():
#     pass
if __name__ == '__main__':
    mcp.run(transport='stdio')