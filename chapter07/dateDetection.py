#! python3
# dateDetection.py - Detecting Dates in strings of text
import re

# Regex for DD/MM/YYYY

dateRegex = re.compile(r'(0?[1-9]|[1-2][0-9]|[3][0-1])\/(0?[1-9]|[1][0-2])\/([1-2][0-9][0-9][0-9])')
mo = dateRegex.search('31/06/2020')

# Variables for Month Day Year
day, month, year = mo.groups()

check = True

if month == '04' or month == '06' or month == '09' or month == '11':
    if day > '30':
        check = False
elif month == '02':
    if day == '29':
        if int(year) % 4 == 0:
            if int(year) % 100 == 0:
                if int(year) % 400 != 0:
                    check = False
        else:
            check = False
    elif day >= '30':
        check = False
else:
    if day > '31':
        check = False
    
print(check)

            


            
