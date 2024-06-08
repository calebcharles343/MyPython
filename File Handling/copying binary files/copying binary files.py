f = open('python1.jpg', 'rb')
data = f.read()


cp = open('python.jpg', 'wb')
cp.write(data)

f.close()
cp.close()

