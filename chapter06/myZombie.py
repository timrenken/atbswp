import zombiedice,random

class Rando:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            if random.randint(1,2) == 1:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoBrainer:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0 
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class TwoShotguns:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0 
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class CutShort:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0
        for i in range(random.randint(1,4)):
            shotgun += diceRollResults['shotgun']
            if shotgun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class BrainsOverShotgun:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0
        brains = 0
        while diceRollResults is not None:
            shotgun += diceRollResults['shotgun']
            brains += diceRollResults['brains']
            if shotgun > brains:
                break
            else:
                diceRollResults = zombiedice.roll()

zombies = (
    Rando(name='Rando'),
    TwoBrainer(name='Two Brainer'),
    TwoShotguns(name='Two Shotguns'),
    CutShort(name='Cut Short'),
    BrainsOverShotgun(name='Brains Over Shotgun')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
