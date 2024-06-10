# Accessor mutators
class Customer:
    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no

    def get_name(self):
        print(self.name)

    def get_phoneNo(self):
        print(self.phone_no)

    def set_phoneNo(self, new_phoneNo):
        self.phone_no = new_phoneNo


cus1 = Customer('Charles', '09024259170')
cus1.get_name()
cus1.get_phoneNo()
cus1.set_phoneNo('09130864030')
cus1.get_phoneNo()