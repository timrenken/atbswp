#! python3
# fillingGaps.py {prefix} - locates gaps in file numbering, then rename the files to close the gaps.
import os, sys, shutil
from pathlib import Path

cwd = Path.cwd()
prefix = sys.argv[1]
counter = 1

for folderName, subfolders, filenames in os.walk(cwd):
    files = len(filenames)
    for filename in filenames:
        if filename.startswith(prefix):
            numExt = filename.split(prefix)[1]
            number,extension = numExt.split('.')
            num = number.split('0')[-1]
            if num == counter:
                continue
            else:
                num = counter
                number = str(num).rjust(3,'0')
                shutil.move(cwd / filename, cwd / str(prefix + number + '.' + extension))
                counter += 1