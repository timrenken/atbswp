#! python3
# selectiveCopy.py {extension} {newFolder} - Walks through a folder tree and searches for files with extension,
# then copies these files to a new folder
import shutil, os, sys
from pathlib import Path

# Variables
ext = sys.argv[1]
newFolder = sys.argv[2]
home = Path.home()

# Walk directories
for folderName, subfolders, filenames in os.walk(home):
    for filename in filenames:
        if filename.endswith(ext):
            print(f'Copying {filename}...')
            shutil.copy(folderName / filename, newFolder / filename)