# spam = ['apples', 'bananas', 'tofu', 'cats']
# len(spam)

spam = ['apples', 'bananas', 'tofu', 'cats']

def list():
    if len(spam) > 0:
        print('You have the following items in your spam list: ', end='')
        for i in range(len(spam) - 1):
            print(spam[i],end=', ')
        print('and ' + spam[-1] + '.')
    elif len(spam) == 1:
        print('You only have ' + spam[0] + ' in your spam list!')
    else:
        print('You do not have anything in your spam list.')

def editList():
    spam = []
    print('You do not have anything in your spam list. Would you like to add something?')
    answer = input()
        if answer == 'yes':
            print('What would you like to add?')
            for x in
        elif answer == 'no':
list()
