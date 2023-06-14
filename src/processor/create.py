import sqlite3


def connect_to_db(item):
    conn = sqlite3.connect("./item.db")
    cursor = conn.cursor()

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS cars(state TEXT,price FLOAT, name TEXT PRIMARY KEY,fuel_type TEXT,transmission TEXT,make TEXT,model TEXT,year INT,condition TEXT,mileage FLOAT,engine_size INT)
    """
    )

    cursor.execute("""REPLACE INTO cars(state,price,name,fuel_type,transmission,make,model,year,condition,mileage,engine_size) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",(item['state'],item['price'],item['name'],item['fuel_type'],item['transmission'],item['make'],item['model'],item['year'],item['condition'],item['mileage'],item['engine_size']))
    print('run sucess')
    conn.commit()


item={"state":"abia","price":234555.43,"name":"fshhdjhd dhhdh 3hd d ","fuel_type":"petrol","transmission":"Automatic","make":"audi","model":"dggsj","year":2009,"condition":"nigerian","mileage":23333.32,"engine_size":344}

connect_to_db(item=item)