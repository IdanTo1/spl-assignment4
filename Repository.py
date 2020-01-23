import atexit
import sqlite3

from DAO import _Employees, _CoffeeStands, _Products, _Suppliers, _Activities
from DTO import *

DB_FILE_NAME = "moncafe.db"


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect(DB_FILE_NAME)
        self.employees = _Employees(self._conn)
        self.coffee_stands = _CoffeeStands(self._conn)
        self.products = _Products(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.activities = _Activities(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        cursor = self._conn.cursor()
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

    def fill_tables(self, init_lines):
        for line in init_lines:
            args = line.split(',')
            args = [arg.strip() for arg in args]  # strip any spaces from the line
            table_type = args.pop(0)
            if table_type == "E":
                employee = Employee(*args)
                self.employees.insert(employee)
            elif table_type == "S":
                supplier = Supplier(*args)
                self.suppliers.insert(supplier)
            elif table_type == "P":
                product = Product(*args, 0)  # 0 for initial quantity
                self.products.insert(product)
            else:  # table_type == "C", valid file assumed, activity is not initialized
                coffee_stand = CoffeeStand(*args)
                self.coffee_stands.insert(coffee_stand)

    def fetch_employees_report(self):
        cursor = self._conn.cursor()
        cursor.execute("""SELECT emp.name, emp.salary, cs.location, sum(ifnull(abs(prod.price * act.quantity), 0))
        FROM ((Employees AS emp
        INNER JOIN Coffee_stands AS cs 
        ON emp.coffee_stand = cs.id)
        LEFT OUTER JOIN (Activities AS act
        INNER JOIN Products AS prod ON act.product_id = prod.id)
        ON act.activator_id = emp.id)
        GROUP BY emp.id, emp.name
        ORDER BY emp.name 
        """)
        return cursor.fetchall()

    def fetch_activities_report(self):
        cursor = self._conn.cursor()
        cursor.execute("""SELECT act.date, prod.description, act.quantity, emp.name, supp.name 
            FROM ((Activities AS act 
            INNER JOIN Products AS prod
            ON act.product_id = prod.id)
            LEFT OUTER JOIN Employees AS emp
            ON act.activator_id = emp.id)
            LEFT OUTER JOIN Suppliers AS supp
            ON act.activator_id = supp.id
            ORDER BY act.date
            """)

        return cursor.fetchall()


repo = _Repository()

atexit.register(repo.close)
