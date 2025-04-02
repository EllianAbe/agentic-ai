import sqlite3
import random
from faker import Faker

# Initialize Faker for random data
fake = Faker()

# Create a SQLite database
DB_PATH = "sample.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create sample tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product TEXT,
    amount REAL,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Insert random data
for _ in range(10):  # 10 users
    name = fake.name()
    email = fake.email()
    age = random.randint(18, 60)
    cursor.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))

for _ in range(20):  # 20 orders
    user_id = random.randint(1, 10)
    product = fake.word()
    amount = round(random.uniform(10, 500), 2)
    cursor.execute(
        "INSERT INTO orders (user_id, product, amount) VALUES (?, ?, ?)", (user_id, product, amount))

# Commit and close
conn.commit()
conn.close()

print("✅ SQLite database 'sample.db' created with random data!")
