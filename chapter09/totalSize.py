import os

totalSize = 0

for filename in os.listdir('/home/tim'):
    print(filename + '|' + str(os.path.getsize(os.path.join('/home/tim/', filename))))
    totalSize = totalSize + os.path.getsize(os.path.join('/home/tim/', filename))

print(totalSize)