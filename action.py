import sys

import DTO
import printdb
from Repository import *


def main(actions_file):
    with open(actions_file, 'r') as f:
        for line in f.readlines():
            args = line.split(',')
            args = [arg.strip() for arg in args]
            activity = DTO.Activity(*args)
            curr_quantity = repo.products.get_quantity(activity.product_id)
            new_quantity = curr_quantity + int(activity.quantity)
            if new_quantity >= 0:
                repo.activities.insert(activity)
                repo.products.update(activity.product_id, activity.quantity)
    printdb.main()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("usage - action.py actions.txt")
    main(sys.argv[1])
