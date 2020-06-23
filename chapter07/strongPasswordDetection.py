#! python3
# strongPasswordDetection.py - 
import re

def checkPassword(password):
    lowerRegex = re.compile(r'[a-z]')
    upperRegex = re.compile(r'[A-Z]')
    numRegex = re.compile(r'\d')
    if len(password) < 8:
        return False

    elif len(lowerRegex.search(password).group()) < 1:
        return False
    
    elif len(upperRegex.search(password).group()) < 1:
        return False

    elif len(numRegex.search(password).group()) < 1:
        return False

    else:
        return True

pw = input()
if checkPassword(pw):
    print("Strong Password")
else:
    print("Weak Password")