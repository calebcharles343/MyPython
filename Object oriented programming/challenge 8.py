# User defined exception

class MinimumBalanceError(Exception):
    pass


class Account:
    accountNumber = 10001

    def __init__(self, name, balance=1000):
        try:
            if balance < 1000:
                raise MinimumBalanceError('Account cannot be created')
        except MinimumBalanceError as err:
            print(err)
        else:

            self.name = name
            self.balance = balance
            self.account_number = Account.accountNumber
            Account.accountNumber += 1

    def deposit(self, new_deposit):
        self.balance += new_deposit

    def withdraw(self, withdraw):
        try:
            if (self.balance - withdraw) < 1000:
                raise MinimumBalanceError('Insufficient Balance! Minimum balance is 1000')
        except MinimumBalanceError as err:
            print(err)

        else:
            self.balance -= withdraw

    def show_details(self):
        print('Name:', self.name)
        print('Account Number:', self.accountNumber)
        print('Balance:', self.balance)


acc1 = Account('Roi Wesley', 2000)
acc1.show_details()
acc1.withdraw(1000)
acc1.show_details()
print(' ')
acc2 = Account('Chris Iliyas', 9000)
acc2.show_details()
acc2.withdraw(1000)
acc2.show_details()
acc2.withdraw(7500)
print(' ')
acc3 = Account('Charles', 500)