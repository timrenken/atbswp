import zipfile, os
from pathlib import Path

p = Path.home()

# Selects Zip File
exampleZip = zipfile.ZipFile(p / 'example.zip')

# Extract all files from Zip
exampleZip.extractall()

# Extract one file from Zip to root directory
exampleZip.extract('spam.txt')

# Extract file from zip to selected directory
exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')

exampleZip.close()