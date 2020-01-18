class _Employees:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, employee):
        self._cursor.execute("""
            INSERT INTO Employees (id, name, salary, coffee_stand) VALUES (?, ?, ?, ?)
        """, [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def print_table(self):
        print("Employees")
        self._cursor.execute("SELECT * FROM Employees ORDER BY Employees.id ASC")
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(one)

    def print_report(self):
        print("Employees report")
        self._cursor.execute("""SELECT emp.name, emp.salary, cs.location, sum(prod.price * act.quantity) 
        FROM ((Employees AS emp
        INNER JOIN Coffee_stands AS cs 
        ON emp.coffee_stand = cs.id)
        INNER JOIN Activities AS act on emp.id = act.activator_id) 
        INNER JOIN Products as prod on act.product_id = prod.id
        ORDER BY emp.name ASC
        """)
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(*one)


class _Suppliers:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, supplier):
        self._cursor.execute("""
            INSERT INTO Suppliers (id, name, contact_information) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.contact_information])

    def print_table(self):
        print("Suppliers")
        self._cursor.execute("SELECT * FROM Suppliers ORDER BY Suppliers.id ASC")
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(one)


class _Products:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, product):
        self._cursor.execute("""
            INSERT INTO Products (id, description, price, quantity) VALUES (?, ?, ?, ?)
        """, [product.product_id, product.description, product.price, product.quantity])

    def print_table(self):
        print("Products")
        self._cursor.execute("SELECT * FROM Products ORDER BY Products.id ASC")
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(one)


class _CoffeeStands:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, coffee_stand):
        self._cursor.execute("""
            INSERT INTO Coffee_stands (id, location, number_of_employees) VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def print_table(self):
        print("Coffee stands")
        self._cursor.execute("SELECT * FROM Coffee_stands ORDER BY Coffee_stands.id ASC")
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(one)


class _Activities:
    def __init__(self, cursor):
        self._cursor = cursor

    def insert(self, activity):
        self._cursor.execute("""
            INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def print_table(self):
        print("Activities")
        self._cursor.execute("SELECT * FROM Activities ORDER BY Activities.date ASC")
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(one)

    def print_report(self):
        print("Activities")
        self._cursor.execute("""SELECT act.date, prod.description, act.quantity, emp.name, supp.name 
        FROM ((Activities AS act 
        INNER JOIN Products AS prod
        ON act.product_id = prod.id)
        LEFT OUTER JOIN Employees AS emp
        ON act.activator_id = emp.id)
        LEFT OUTER JOIN Suppliers AS supp
        ON act.activator_id = supp.id
        ORDER BY act.date DESC 
        """)
        all_data = self._cursor.fetchall()
        for one in all_data:
            print(one)
