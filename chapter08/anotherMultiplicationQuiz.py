import random, time

numberOfQuestions = 10
correctAnswers = 0
timeout = 8


for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    question = str(num1) + " x " + str(num2) + " = "
    incorrectAnswers = 0
    for attempts in range(3):
        endTime = time.time() + timeout
        answer = input(question)
        try:
            if time.time() < endTime:
                if int(answer) == num1*num2:
                    print('Correct!')
                    correctAnswers += 1
                    pass
                else:
                    print('Incorrect, try again.')
                    incorrectAnswers += 1
                    continue
            else:
                print('Out of time!')
        except ValueError:
            print('Incorrect, try again.')
            incorrectAnswers += 1            
        break
        
    if incorrectAnswers == 3:
        print('Out of tries!')
        


print('Score: ' + str(correctAnswers) + ' / ' + str(numberOfQuestions))