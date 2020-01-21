import os

from Repository import *


def print_employees_report():
    print("Employees report")
    all_data = repo.fetch_employees_report()
    for one in all_data:
        print(*one)


def print_activities_report():
    print("Activities")
    all_data = repo.fetch_activities_report()
    for one in all_data:
        print(one)


def print_table(dao):
    all_data = dao.fetch_table()
    for one in all_data:
        print(one)


def main():
    # multiple reads because no generic read is possible
    print("Activities")
    print_table(repo.activities)
    print("Coffee stands")
    print_table(repo.coffee_stands)
    print("Employees")
    print_table(repo.employees)
    print("Products")
    print_table(repo.products)
    print("Suppliers")
    print_table(repo.suppliers)
    print()  # blank line between tables and reports
    print_employees_report()
    print()  # blank line between reports
    print_activities_report()


if __name__ == "__main__":
    db_exists = os.path.isfile(DB_FILE_NAME)
    if not db_exists:
        raise FileNotFoundError(("data base %s does not exists" % DB_FILE_NAME))
    main()
