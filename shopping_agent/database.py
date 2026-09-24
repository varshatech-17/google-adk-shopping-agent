import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).parent / "students.db"


connection = sqlite3.connect(DATABASE_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    attendance REAL
)
""")

students = [
    (1, "Aarav", 92),
    (2, "Diya", 68),
    (3, "Rohan", 74),
    (4, "Sneha", 88),
    (5, "Kabir", 71)
]

cursor.executemany(
    "INSERT OR REPLACE INTO students VALUES (?, ?, ?)",
    students
)

connection.commit()
connection.close()

print("Students database created successfully!")