# Project 2: Yahtzee
import random


class Single_Dice:
    """Yahtzee Dice game"""
    def __init__(self, side):
        """Describes characterisctics of the yahtzee"""
        self.side=side
        self.face = 1



    def roll(self):
        """Gets=as a random number between 1 and 6"""
        self.side = random.randint(1, self.side)
       

    def getCurrentFaceValue(self):
        """Get the value currently showing on the die face"""
        return self.side



    def showDieFace(self):
        """ Display the value currently showing on the die."""
        print(f'{self.side}')

class Player(Single_Dice):
    def __init__(self, side):
        super().__init__(side)
        """New Player"""


    def roll_dice(self):
        Player.roll()


    def getCurrentFaceValue(self):
        return super().getCurrentFaceValue()


    def showDieFace(self):
        return super().showDieFace()



die1 = Player(6)
die1.roll()
die2 = Player(6)
die2.roll()
die3 = Player(6)
die3.roll()
die4 = Player(6)
die4.roll()
die5 = Player(6)
die5.roll()
player = [die1.side, die2.side, die3.side, die4.side, die5.side]
str1 = ''.join(str(e) for e in player)

def play():
   for s in str1:
        print(f'({s})', end="")
print()


def yahtzee():
   for x in str1:
    if str1.count(x) == 2:
        print('\nYAHTZEE')
        break
play()
yahtzee()