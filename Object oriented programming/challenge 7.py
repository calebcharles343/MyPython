# Accessor mutators

class CurrencyConverter:
    def __init__(self, currency, rate):
        self.currency = currency
        self.rate = rate

    def set_currency(self, new_currency):
        self.currency = new_currency

    def get_currency(self):
        print(self.currency)

    def set_rate(self, new_rate):
        self.rate = new_rate

    def get_rate(self):
        print(self.rate)

    def convert(self, amount):
        return amount * self.rate

convert = CurrencyConverter('USD', 1500)
print(convert.convert(1000))

convert.set_currency('EUR')
convert.set_rate(1200)
print(convert.convert(1000))