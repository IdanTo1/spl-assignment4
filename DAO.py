class _Employees:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, employee):
        self._cursor.execute("""
            INSERT INTO employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
        """, [employee.id, employee.name, employee.salary, employee.coffee_stand])


class _Suppliers:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, supplier):
        self._cursor.execute("""
            INSERT INTO suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])


class _Products:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, product):
        self._cursor.execute("""
            INSERT INTO products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.product_id, product.description, product.price, product.quantity])


class _CoffeeStands:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, coffee_stand):
        self._cursor.execute("""
            INSERT INTO coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])


class _Activities:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, activity):
        self._cursor.execute("""
            INSERT INTO activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])
