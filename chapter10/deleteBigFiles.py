#! python3
# deleteBigFiles.py - Doesn't delete but prints out the absolute path of files bigger than 100MB

import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\Tim'):
    for filename in filenames:
        fileSize = os.path.getsize(folderName + '\\' + filename)
        if fileSize > 1024*1024*1024:
            print(f'{folderName}\\{filename} = {round(fileSize/(1024*1024*1024),2)}GB')