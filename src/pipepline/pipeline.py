import sqlite3

conn = sqlite3.connect("item.db")

cursor = conn.cursor()

cursor.execute(
    """ CREATE TABLE cars(state TEXT,price FLOAT, name TEXT,fuel_type TEXT,transmission TEXT,make TEXT,model TEXT,year INT,condition TEXT,millage FLOAT,engine_size INT)
"""
)
