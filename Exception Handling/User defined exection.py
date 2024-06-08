class MyError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __int__(self):
        return  self.msg
try:
    raise MyError('Some Error')
except MyError as e:
    print(e)