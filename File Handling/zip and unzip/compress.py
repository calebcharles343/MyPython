# import zipfile
# f = zipfile.ZipFile('images.zip', 'w', zipfile.ZIP_DEFLATED)
#  OR

from zipfile import *
f = ZipFile('images.zip', 'w', ZIP_DEFLATED)

f.write('csharp.jpg')
f.write('java.jpg')
f.write('cpp.jpg')
f.write('javascript.jpg')
f.write('python.jpg')

f.close()