import sqlite3

def save_to_db(item):
    try:
        conn = sqlite3.connect("./item.db")
        cursor = conn.cursor()

        cursor.execute(
            """ CREATE TABLE IF NOT EXISTS cars(state TEXT,price FLOAT, name TEXT PRIMARY KEY,fuel_type TEXT,transmission TEXT,make TEXT,model TEXT,year INT,condition TEXT,mileage FLOAT,engine_size INT)
        """
        )

        cursor.executemany("""REPLACE INTO cars(state,price,name,fuel_type,transmission,make,model,year,condition,mileage,engine_size) VALUES (?,?,?,?,?,?,?,?,?,?,?)""",item)
        print('run sucess')
        conn.commit()
    except Exception as e:
        print(f'db error {e}')
