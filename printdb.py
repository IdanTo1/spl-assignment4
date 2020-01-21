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


def main():
    # multiple reads because no generic read is possible
    repo.activities.print_table()
    repo.coffee_stands.print_table()
    repo.employees.print_table()
    repo.products.print_table()
    repo.suppliers.print_table()
    print()  # blank line between tables and reports
    print_employees_report()
    print()  # blank line between reports
    print_activities_report()


if __name__ == "__main__":
    db_exists = os.path.isfile(DB_FILE_NAME)
    if not db_exists:
        raise FileNotFoundError(("data base %s does not exists" % DB_FILE_NAME))
    main()
