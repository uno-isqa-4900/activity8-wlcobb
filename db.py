import csv
from business import Customer

FILENAME = 'customers.csv'


def get_customer(self):
    customers = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            customers.append(customer)
    return customers