## Author: Kasonde Besa
## Date: June 15th 2020
## Description: The idea is to ride your camel across the desert while being chased. You need to manage your thirst, 
## how tired the camel is, and how far ahead of the natives you are.
from random import randint

#(String) -> (Boolean)
def choice(moveChoice):
    """Executes user's move choice"""
    gameState = False
    global thirst
    global canteenDrinks 
    global milesTraveled
    global nativesMiles
    global tiredness
    global oasis
    
    # Quit camel game
    if moveChoice.lower() == 'q':
        print("You quit, Game Over!")
        gameState = True
    
    # Drink from canteen
    elif moveChoice.lower()=='a':
        if canteenDrinks>0:
            canteenDrinks -=1
            thirst = 0
            print("Uhhh... refreshing!")
        else:
            print("Out of drinks!")

    # Go ahead moderate speed
    elif moveChoice.lower() == 'b':
        distanceMoved = randint(5,13)
        print("You traveled",distanceMoved,"miles.")
        thirst += 1
        tiredness += 1
        nativesMiles += randint(7,15)

    # Go ahead full speed
    elif moveChoice.lower() == 'c':
        distanceMoved = randint(10,21)
        milesTraveled += distanceMoved
        print("You traveled",distanceMoved,"miles.")
        thirst += 1
        tiredness += randint(1,3)
        nativesMiles += randint(7,15)
    
    # Stop for the night
    elif moveChoice.lower() == 'd':
        tiredness = 0
        print("This camel is happy and well rested.")
        nativesMiles += randint(7,15)

    # Show user status in game
    elif moveChoice.lower() == 'e':
        print("Miles traveled:",milesTraveled)
        print("Drinks in canteen:", canteenDrinks)
        print("The natives are",(milesTraveled - nativesMiles),"miles behind you") 
    oasis = randint(1,21)
    if oasis == 7 and moveChoice!='e':
        canteenDrinks = 3
        print("Lucky you! You found an oasis and refilled your canteen!")
    return gameState

#(void)->(void)
def moveOptions():
    """Allows player to see possible moves"""   
    print("\nA. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

#(void)->(void)
def main():
    """ Runs the game"""
    done = False
    while not done:
        moveOptions()
        moveChoice = input("Your choice? ")
        print("")
        gameState = choice(moveChoice)
        if gameState == True:
            break
        if thirst > 4:
            print("You are thirsty.")
        if thirst > 6:
            print("You died of thirst!")
            break
        if tiredness > 5:
            print("Your camel is getting tired.")
        if tiredness>8:
            print("Your camel is dead")
            break
        if nativesMiles>=milesTraveled:
            print("They caught up to you... Game over!")
            break
        if milesTraveled - nativesMiles < 15:
            print("The natives are getting close!")
        if milesTraveled >=200:
            print("You made it across the desert! You won!")
            break

if __name__ == '__main__':
    print("Welcome to my Camel Game!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their came back and are chasing you down!")
    print("Surive your desert trek and outrun the natives.")
    thirst = 0
    tiredness = 0
    canteenDrinks = 3
    milesTraveled = 0
    nativesMiles = -20
    oasis = 0
    main()