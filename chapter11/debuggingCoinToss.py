#! python3

import random,logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

guess = ''
while guess not in ('heads','tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    if guess.lower() not in ('tails', 'heads'):
        raise Exception('You must guess "heads" or "tails".')
    logging.debug(f"The user's guess is {guess}")
toss = random.randint(0,1) # 0 is tails, 1 is heads
logging.debug(f'The toss is {str(toss)}.')
if toss == guess.lower():
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    logging.debug(f"The user's guess is {guess}")
    if toss == guess.lower():
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
        
logging.debug('End of program')