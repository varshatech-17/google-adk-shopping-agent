import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).parent / "students.db"


def search_products(category: str, max_price: float):
    """Search for products in a category within the user's maximum budget."""

    products = [
        {"name": "Laptop A", "category": "laptop", "price": 45000},
        {"name": "Laptop B", "category": "laptop", "price": 55000},
        {"name": "Laptop C", "category": "laptop", "price": 65000},
        {"name": "Headphones A", "category": "headphones", "price": 3000},
        {"name": "Headphones B", "category": "headphones", "price": 5000},
    ]

    results = [
        product
        for product in products
        if product["category"].lower() == category.lower()
        and product["price"] <= max_price
    ]

    return results


def get_students_below_attendance(limit: float):
    """Get students whose attendance is below the given percentage."""

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT name, attendance FROM students WHERE attendance < ?",
        (limit,)
    )

    results = cursor.fetchall()

    connection.close()

    return results