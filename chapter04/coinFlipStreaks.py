import random

numberOfStreaks = 0
flipResults = []
streak = 0

for experimentNumber in range(10000):
    for flips in range(100):
        flip = random.randint(0,1)
        if flip == 0:
            flipResults.append('T')
        else:
            flipResults.append('H')
    for i in range(len(flipResults)):
        if flipResults[i] == flipResults[i - 1]:
            streak += 1
            if streak >= 6:
                numberOfStreaks += 1
                streak = 0
        else:
            streak = 0

    flipResults = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100))