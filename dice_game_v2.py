import random
import time

def diceroll(sides):  
    dice = random.randrange(sides)
    return dice       
def nameprompt():
    p1 = input("Enter players name: ")
    return p1
def gameplay():
    rollone = diceroll(10) + diceroll(6)
    print(rollone)
    return rollone
def gameresult(rollone, rolltwo):
    if rollone > rolltwo:
        print ("Player One Wins!")
    elif rolltwo > rollone:
        print ("Player Two Wins!")
    else:
        print ("you tied")
def play_again():
    playagain = input("play again? y/n: ")
    if playagain.lower() == "n":
        print ("Goodbye.")
        exit()
    elif playagain.lower() == "y":  
        print ("Sorry, that feature is not available.  Nobody has ever said yes before!  Goodbye.")
        time.sleep(3)
    else: 
        print("try again... ")
        
    
player1 = nameprompt()
player1r1 = gameplay() + gameplay()
print ("Player 1 rolls two dice for a total score of.............................")
print (player1r1)
player2 = nameprompt()
player2r1 = gameplay() + gameplay()
print ("Player 2 rolls two dice for a total score of.............................")
print (player2r1)
gameresult(player1r1,player2r1)
play_again()

    
    
