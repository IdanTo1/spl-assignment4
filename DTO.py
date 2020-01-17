class Employee:
    def __init__(self, employee_id, name, salary, coffee_stand):
        self.id = employee_id
        self.name = name
        self.salary = salary
        self.coffee_stand = coffee_stand


class Supplier:
    def __init__(self, supplier_id, name, contact_information):
        self.id = supplier_id
        self.name = name
        self.contact_information = contact_information


class Product:
    def __init__(self, product_id, description, price, quantity):
        self.product_id = product_id
        self.description = description
        self.price = price
        self.quantity = quantity


class CoffeeStand:
    def __init__(self, coffee_stand_id, location, number_of_employees):
        self.id = coffee_stand_id
        self.location = location
        self.number_of_employees = number_of_employees


class Activity:
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date
