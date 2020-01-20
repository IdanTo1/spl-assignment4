import os
import sqlite3

from DAO import _Employees, _Suppliers, _Products, _CoffeeStands, _Activities
from DTO import *


def print_employees_report(cursor):
    print("Employees report")
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

    all_data = cursor.fetchall()
    for one in all_data:
        print(*one)


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
    ORDER BY act.date
    """)
    all_data = cursor.fetchall()
    for one in all_data:
        print(one)


def main(cursor):
    _Activities(cursor).print_table()
    _CoffeeStands(cursor).print_table()
    _Employees(cursor).print_table()
    _Products(cursor).print_table()
    _Suppliers(cursor).print_table()
    print()
    print_employees_report(cursor)
    print()
    print_activities_report(cursor)


if __name__ == "__main__":
    db_exists = os.path.isfile(DB_FILE_NAME)
    if not db_exists:
        raise FileNotFoundError(("data base %s does not exists" % DB_FILE_NAME))
    db_conn = sqlite3.connect(DB_FILE_NAME)
    db_cursor = db_conn.cursor()
    main(db_cursor)
    db_conn.close()
