import sqlite3
import sys

from DAO import _Employees, _Suppliers, _Products, _CoffeeStands
from DTO import *


def create_tables(cursor):
    cursor.execute("""CREATE TABLE Employees(id INTEGER PRIMARY KEY,
                                                name TEXT NOT NULL,
                                                salary REAL NOT NULL,
                                                coffee_stand INTEGER REFERENCES Coffee_stands(id))
    
    """)
    cursor.execute("""CREATE TABLE Suppliers(id INTEGER PRIMARY KEY,
                                                name TEXT NOT NULL,
                                                contact_information TEXT)
    """)
    cursor.execute("""CREATE TABLE Products(id INTEGER PRIMARY KEY,
                                                description TEXT NOT NULL,
                                                price REAL NOT NULL,
                                                quantity INTEGER NOT NULL)
    """)
    cursor.execute("""CREATE TABLE Coffee_stands(id INTEGER PRIMARY KEY,
                                                    location TEXT NOT NULL,
                                                    number_of_employees INTEGER)
    """)
    cursor.execute("""CREATE TABLE Activities(product_id INTEGER REFERENCES Products(id),
                                                quantity INTEGER NOT NULL,
                                                activator_id INTEGER NOT NULL,
                                                date DATE NOT NULL)
    """)


def fill_tables(cursor, config_file):
    employees = _Employees(cursor)
    suppliers = _Suppliers(cursor)
    products = _Products(cursor)
    coffee_stands = _CoffeeStands(cursor)
    with open(config_file, "r") as f:
        for line in f.readlines():
            args = line.split(',')
            args = [arg.strip() for arg in args]  # strip any spaces from the line
            table_type = args.pop(0)
            if table_type == "E":
                employee = Employee(*args)
                employees.insert(employee)
            elif table_type == "S":
                supplier = Supplier(*args)
                suppliers.insert(supplier)
            elif table_type == "P":
                product = Product(*args)
                products.insert(product)
            else:  # table_type == "C", valid file assumed, activity is not initialized
                coffee_stand = CoffeeStand(*args)
                coffee_stands.insert(coffee_stand)


def main(config_file):
    open(DB_FILE_NAME, 'w').close()  # clear the db file

    db_conn = sqlite3.connect(DB_FILE_NAME)
    db_cursor = db_conn.cursor()
    create_tables(db_cursor)
    fill_tables(db_cursor, config_file)

    db_conn.commit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("uasge - initiate.py config.txt")
    main(sys.argv[1])
