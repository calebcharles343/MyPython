class Customer:
    def __init__(self, id, name, bdno, bstreet, bcity, bcountry, bpin, sdno, sstreet, scity, scountry, sPin):
        self.customerId = id
        self.name = name
        self.baddress = self.Address(bdno, bstreet, bcity, bcountry, bpin)
        self.saddress = self.Address(sdno, sstreet, scity, scountry, sPin)

    class Address:
        def __init__(self, doorNo, street, city, country, pin):
            self.doorNo = doorNo
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin
        def display(self):
            print(self.doorNo)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)

c = Customer(10, 'Charles', 1, 'abc', 'Abujs', 'Nigeria', 900231, 'xyx', 'Adamawa', 'Nigeria', 900101, 101)

print('####=> BILLING ADDRESS')
c.baddress.display()

print('####=> SHIPING ADDRESS')
c.saddress.display()

