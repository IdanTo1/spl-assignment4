import os
import sqlite3

from DAO import _Employees, _Suppliers, _Products, _CoffeeStands, _Activities
from DTO import *


def print_employees_report(cursor):
    print("Employees report")
    cursor.execute("""SELECT emp.name, emp.salary, cs.location, sum(prod.price * act.quantity)
    FROM ((Employees AS emp
    INNER JOIN Coffee_stands AS cs 
    ON emp.coffee_stand = cs.id)
    LEFT OUTER JOIN (Activities AS act
    INNER JOIN Products AS prod ON act.product_id = prod.id)
    ON act.activator_id = emp.id)
    GROUP BY emp.id
    """)

    all_data = cursor.fetchall()
    for one in all_data:
        print(*one)


# , sum(prod.price * act.quantity)
# LEFT OUTER JOIN (Activities AS act
#     INNER JOIN Products as prod on act.product_id = prod.id)
#     ON emp.id = act.activator_id)
#   ON emp.id = act.activator_id
#   ORDER BY emp.name ASC


def print_activities_report(cursor):
    print("Activities")
    cursor.execute("""SELECT act.date, prod.description, act.quantity, emp.name, supp.name 
    FROM ((Activities AS act 
    INNER JOIN Products AS prod
    ON act.product_id = prod.id)
    LEFT OUTER JOIN Employees AS emp
    ON act.activator_id = emp.id)
    LEFT OUTER JOIN Suppliers AS supp
    ON act.activator_id = supp.id
    ORDER BY act.date ASC
    """)
    all_data = cursor.fetchall()
    for one in all_data:
        print(one)


def main():
    db_exists = os.path.isfile(DB_FILE_NAME)
    if not db_exists:
        raise FileNotFoundError(("data base %s does not exists" % DB_FILE_NAME))
    db_conn = sqlite3.connect(DB_FILE_NAME)
    db_cursor = db_conn.cursor()

    db_cursor.execute("""INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
                """, [9004, 100, 102, 20001010])
    db_cursor.execute("""INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
        """, [9002, 10, 1004, 20001010])
    db_cursor.execute("""INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
            """, [9002, 30, 1004, 20001011])
    db_cursor.execute("""INSERT INTO Activities (product_id, quantity, activator_id, date) VALUES (?, ?, ?, ?)
            """, [9004, 20, 1003, 20001010])

    _Activities(db_cursor).print_table()
    _CoffeeStands(db_cursor).print_table()
    _Employees(db_cursor).print_table()
    _Products(db_cursor).print_table()
    _Suppliers(db_cursor).print_table()
    print()
    print_employees_report(db_cursor)
    print()
    print_activities_report(db_cursor)


if __name__ == "__main__":
    main()
