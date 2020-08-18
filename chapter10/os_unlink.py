import os
from pathlib import Path


# Deletes all files with extension (Prints the names instead)
for filename in Path.home().glob('*.rxt'):
    # os.unlink(filename)
    print(filename)