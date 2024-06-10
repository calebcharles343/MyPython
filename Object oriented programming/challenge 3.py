# write a class for book

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def show_details(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Price:', self.price)

bi = Book('It', 'Steven King', "$200")
b2 = Book('1408', 'Steven King', "$150")
bi.show_details()
print(' ')
b2.show_details()
