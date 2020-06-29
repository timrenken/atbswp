import pyinputplus as pyip

prices = {"wheat": 0.25, "white": 0.30, "sourdough": 0.35,
"chicken": 0.50, "turkey": 0.70, "ham": 0.60, "tofu": 0.80,
"cheddar": 0.20, "swiss": 0.25, "mozzarella": 0.30, "mayo": 0.05,
"mustard": 0.05, "lettuce": 0.05, "tomato": 0.05, 'gluten-free': 0.30}

breadTypes = ['wheat','white','sourdough','gluten-free']
proteinTypes = ['chicken','turkey','ham','tofu']
cheeseTypes = ['cheddar','swiss','mozzarella']

def sandwichBuilder(num):
    sandwich = []
    # Asking for ingredients, and adding them to the sandwich list
    sandwich.append(pyip.inputMenu(breadTypes))
    sandwich.append(pyip.inputMenu(proteinTypes))
    if pyip.inputYesNo('Would you like Cheese? ') == 'yes':
        sandwich.append(pyip.inputMenu(cheeseTypes))
    if pyip.inputYesNo('Would you like Mayo? ') == 'yes':
        sandwich.append('mayo')
    if pyip.inputYesNo('Would you like mustard? ') == 'yes':
        sandwich.append('mustard')
    if pyip.inputYesNo('Would you like Lettuce? ') == 'yes':
        sandwich.append('lettuce')
    if pyip.inputYesNo('Would you like Tomato? ') == 'yes':
        sandwich.append('tomato')
    return sandwich

numOfSandwiches = pyip.inputInt('How many Sandwiches would you like? ')

sandwiches = []
totalCost = 0.00

for s in range(numOfSandwiches):
    sandwiches.append(sandwichBuilder(s))

for n in range(len(sandwiches)):
    total = 0.00
    for p in range(len(sandwiches[n])):
        total += prices[sandwiches[n][p]]
    totalCost += total
    print("\n" + sandwiches[n][1] + " sandwich on " + sandwiches[n][0] +
    ' bread with ' + str(len(sandwiches[n])-2) + ' toppings, costs $' +
    str(round(total, 2)))

if len(sandwiches) > 1:
    print("\nYour total is $" + str(round(totalCost, 2)))