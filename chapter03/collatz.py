import sys


def collatz(number):
    global userNumber
    if number % 2 == 0:
        userNumber = number // 2

    elif number % 2 == 1:
        userNumber = 3 * number + 1

userNumber = 0

while True:
    print('Enter number')
    userNumber = int(input())
    while True:
        print(userNumber)
        if userNumber == 1:
            sys.exit()
        elif userNumber > 1:
            collatz(userNumber)