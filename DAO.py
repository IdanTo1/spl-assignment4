from DTO import *


class _Employees:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, employee):
        cursor = self._conn.cursor()
        self._cursor.execute("""
            INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
        """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def find_all(self):
        self._cursor.execute("SELECT * FROM Employees ORDER BY Employees.id")
        return [Employee(*row) for row in self._cursor.fetchall()]


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, supplier):
        self._cursor.execute("""
            INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def find_all(self):
        self._cursor.execute("SELECT * FROM Suppliers ORDER BY Suppliers.id")
        return [Supplier(*row) for row in self._cursor.fetchall()]


class _Products:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, product):
        self._cursor.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.id, product.description, product.price, product.quantity])

    def find_all(self):
        self._cursor.execute("SELECT * FROM Products ORDER BY Products.id")
        return [Product(*row) for row in self._cursor.fetchall()]

    def update(self, product):
        self._cursor.execute("""UPDATE Products SET quantity = quantity + ?
        WHERE id = ?""", [product.quantity, product.id])

    def find(self, product_id):
        self._cursor.execute("""SELECT * FROM Products
                    WHERE id = ?
                    """, [product_id])
        data = self._cursor.fetchone()
        return Product(*data)


class _CoffeeStands:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, coffee_stand):
        self._cursor.execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find_all(self):
        self._cursor.execute("SELECT * FROM Coffee_stands ORDER BY Coffee_stands.id")
        return [CoffeeStand(*row) for row in self._cursor.fetchall()]


class _Activities:
    def __init__(self, conn):
        self._conn = conn
        self._cursor = self._conn.cursor()

    def insert(self, activity):
        self._cursor.execute("""
            INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find_all(self):
        self._cursor.execute("SELECT * FROM Activities ORDER BY Activities.date")
        return [Activity(*row) for row in self._cursor.fetchall()]
