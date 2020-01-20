import sqlite3
import sys

import printdb
from DAO import _Activities, _Products
from DTO import *


def main(actions_file):
    db_conn = sqlite3.connect(DB_FILE_NAME)
    db_cursor = db_conn.cursor()
    with open(actions_file, 'r') as f:
        for line in f.readlines():
            args = line.split(',')
            args = [arg.strip() for arg in args]
            activity = Activity(*args)
            curr_quantity = _Products(db_cursor).get_quantity(activity.product_id)
            new_quantity = curr_quantity + int(activity.quantity)
            if new_quantity >= 0:
                _Activities(db_cursor).insert(activity)
                _Products(db_cursor).update(activity.product_id, activity.quantity)
    db_conn.commit()
    printdb.main(db_cursor)
    db_conn.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("usage - action.py actions.txt")
    main(sys.argv[1])
