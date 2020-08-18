import send2trash

baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

# Sends file to Recycle Bin
send2trash.send2trash('bacon.txt')