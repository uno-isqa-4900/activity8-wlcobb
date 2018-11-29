class Customer:
    def __init__(self, cust_id='', first_name='', last_name='', company_name='', address='', city='', state='', zip=''):
        self.cust_id = cust_id
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        pass
#returning the address of the customer in a method
    def get_address(self):
        # if Customer does not have company attribute, don't return company in string
        if (self.company_name == ''):
            return self.first_name + " " + self.last_name + '\n' + self.address + '\n' + self.city + ', ' + self.state + ' ' + self.zip
        else:
            return self.first_name + ' ' + self.last_name + '\n' + self.company_name + '\n' + self.address + '\n' + self.city + ', ' + self.state + ' ' + self.zip



