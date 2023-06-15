import sqlite3


def connect_to_db(item):
    conn = sqlite3.connect("./item.db")
    cursor = conn.cursor()

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS cars(state TEXT,price FLOAT, name TEXT PRIMARY KEY,fuel_type TEXT,transmission TEXT,make TEXT,model TEXT,year INT,condition TEXT,mileage FLOAT,engine_size INT)
    """
    )

    conn.executemany("""REPLACE INTO cars(state,price,name,fuel_type,transmission,make,model,year,condition,mileage,engine_size) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",item)
    print('run sucess')
    conn.commit()


item=[('abia state',234555.43,"fshjjjjhd dhhdh 3hd d ","petrol","Automatic",
       "audi","dggsj",2009,"nigerian",23333.32,344),("abia lagos",234555.43,"fsqwwdjhd dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjhd dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjyu7d dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjhd dqhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjhd rthhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjhd dheeh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc b3e dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjhd chdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"hjgc bbjhd dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bjhd dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"hjgc bbjhd dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"bjhd dhhdh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344),("abia",234555.43,"fshjgc bbjh 3hd d ","petrol","Automatic","audi","dggsj",2009,"nigerian",23333.32,344)]

print(len(item))
connect_to_db(item=item)