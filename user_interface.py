import db
from business import Customer


def display_message():
    print("Customer Viewer")
    print()


#this is where I am looking for the correct customer id.
def find_customer(id):
    customers = db.get_customer(Customer)
#i want to be able to loop through the db to find this.  I keep getting error. If I do not do the 100, the numbers are off.
#subtracting the 100 puts it to where they are in the index.  Saw this in the book.
    if id>= 101 and id <=600:
        customer = customers[id-100]
        print(customer.get_address())

    else:
        print("No customer with that ID")




def main():
    print ()
    display_message()

choice = 'y'
id=''
main()

while choice.lower() == 'y':
    id = int(input("Enter customer ID: "))
    (find_customer(id))
    print()
    choice = input("Continue (y/n)")
    print()

print("Bye!")






#if __name__ == '__main__'
