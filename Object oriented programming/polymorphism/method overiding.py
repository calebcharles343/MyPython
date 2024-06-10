class IphoneVI:
    def home(self):
        print('home button is pressed')


class IphoneX(IphoneVI):
    def home(self):
        print('home is touched')
        super().home()


# iphone6 = IphoneVI()
# iphone6.home()

iphone10 = IphoneX()
iphone10.home()

