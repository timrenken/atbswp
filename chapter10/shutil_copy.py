import shutil, os
from pathlib import Path

p = Path.home()

# Copies files to a directory
shutil.copy(p / 'spam.txt', p / 'some_folder')

# Copies file to a directory with a new name
shutil.copy(p / 'eggs.txt', p / 'some_folder/eggs2.txt')

# Copies a directory and it's content
shutil.copytree(p / 'spam', p / 'spam_backup')