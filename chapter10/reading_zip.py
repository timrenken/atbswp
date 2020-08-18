import zipfile, os
from pathlib import Path

p = Path.home()
exampleZip = zipfile.ZipFile(p / 'example.zip')

# Gets contents of zip file
exampleZip.namelist()

# Gets infomation about a file that is compressed
spamInfo = exampleZip.getinfo('spam.txt')

# True file size
spamInfo.file_size

# Compressed file size
spamInfo.compress_size

print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!')

exampleZip.close()