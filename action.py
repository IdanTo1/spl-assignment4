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
            product = repo.products.find(activity.product_id)
            curr_quantity = int(product.quantity)
            new_quantity = curr_quantity + int(activity.quantity)
            if new_quantity >= 0:
                repo.activities.insert(activity)
                product.quantity = new_quantity
                repo.products.update(product)
    printdb.main()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("usage - action.py actions.txt")
    main(sys.argv[1])
