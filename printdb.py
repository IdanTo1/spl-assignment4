import os
import sqlite3

from DAO import _Employees, _Suppliers, _Products, _CoffeeStands, _Activities
from DTO import *


def main():
    db_exists = os.path.isfile(DB_FILE_NAME)
    if not db_exists:
        raise FileNotFoundError(("data base %s does not exists" % DB_FILE_NAME))
    db_conn = sqlite3.connect(DB_FILE_NAME)
    db_cursor = db_conn.cursor()
    _Activities(db_cursor).print_table()
    _CoffeeStands(db_cursor).print_table()
    _Employees(db_cursor).print_table()
    _Products(db_cursor).print_table()
    _Suppliers(db_cursor).print_table()
    print()
    _Employees(db_cursor).print_report()
    print()
    _Activities(db_cursor).print_report()


if __name__ == "__main__":
    main()
