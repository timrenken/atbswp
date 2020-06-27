#! python3
import re

def stripMethod(string,strip=None):
    if strip == None:
        stripLeft = re.compile(r'^\s*')
        stripRight = re.compile(r'\s*$')
    else:
        stripLeft = re.compile(r'^['+re.escape(strip)+']*')
        stripRight = re.compile(r'['+re.escape(strip)+']*$')
    string = re.sub(stripLeft, "", string)
    string = re.sub(stripRight, "", string)
    return string


print(stripMethod("   Hello world!   "))

print(stripMethod('***Hello world! I am taking this over!***', '*'))




