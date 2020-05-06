from cmd import Cmd
import random as rand

currentCardPool = []

class card():
    
    def __init__(self, number, numberInEnglish, suit, point):
        self.number = number
        self.numberInEnglish = numberInEnglish
        self.suit = suit
        self.point = point
        
    def __str__(self):
        return "%s of %s"  % (self.number, self.suit)

currentCardPool = []

def dealcard():
    number = rand.randint(1, 13)
    numberInEnglish = number
    point = number
    if number == 1:
        numberInEnglish = 'Ace'   
    if number == 11:
        numberInEnglish = 'Jack'   
        point = 10
    if number == 12:
        numberInEnglish = 'Queen'
        point = 10
    if number == 13:
        numberInEnglish = 'King'
        point = 10
        
    suitNum = rand.randint(1,4)
    if suitNum == 1:
        suit = 'Spade'
    if suitNum == 2:
        suit = 'Heart'
    if suitNum == 3:
        suit = 'Clover'
    if suitNum == 4:
        suit = 'Diamond'
        
    newCard = (number, numberInEnglish, suit, point)
    if newCard in currentCardPool:
        dealcard()
    else:
        currentCardPool.append(newCard)


class MyPrompt(Cmd):
    dealcard()
    dealcard()
    dealcard()
    dealcard()

    
    prompt = 'user> '
    intro = 'Dealer is showing:', currentCardPool[0], 'You are holding:', currentCardPool[2], currentCardPool[3]

    def do_exit(self, inp):
        print("Bye")
        return True
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
    
        
    def do_hit(self, inp):
        dealcard()
        currentValue = sum(x[3] for x in currentCardPool)
        if (currentValue>21):
            print("you drew", currentCardPool[-1])
            print("You Bust")
            return True
        else:
            print(currentCardPool[-1])
            
    def do_score(self, inp):
        yourScore = sum(x[3] for x in currentCardPool)
        dealerScore = sum(x[3] for x in currentCardPool)
        if yourScore > dealerScore:
            print("you win!", yourScore, "to", dealerScore)
            return True
        elif yourScore == dealerScore:
            print("you tie", yourScore, "to", dealerScore)
            return True
        else:
            print("you lose", yourScore, "to", dealerScore)
            return True
            
    
if __name__ == '__main__':
    MyPrompt().cmdloop()
    

