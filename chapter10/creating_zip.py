import zipfile

# Opens new zip file with write permissions
newZip = zipfile.ZipFile('new.zip', 'w')

# Adds file to zip 
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

newZip.close()