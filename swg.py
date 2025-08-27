import random

def computer():
    return random.choice(["snake", "water", "gun"])
    
def getresult(uc, cc):
    if ((uc == "snake") and (cc == "water")):
        print("Snake Crossed the Water E>\n")
        return "Won"
    elif ((uc == "water") and (cc == "gun")):
        print("Water drowned the Gun :->\n")
        return "Won"
    elif ((uc == "gun") and (cc == "snake")):
        print("Gun killed the Snake :-;")
        return "Won"
    elif (uc == cc):
        print("Both choosed the same :-)\n")
        return "Drawn"
    else:
        print("You weren't lucky :-(")
        return "Lost"

def Game():
    while True:
        userchoice = input("Enter your choice: Snake/Water/Gun\n"  ).lower()
        if userchoice not in ["snake", "water", "gun"]:
            userchoice = input("Please enter \"snake\" or \"water\" or \"gun\":\n ")
        computerchoice = computer()
        print(f"Choice of User: {userchoice.capitalize()}")
        print(f"Choice of Computer: {computerchoice.capitalize()}")
        result = getresult(userchoice, computerchoice)
        print(f"You have {result}")
        play = input("Do you want to play again: y/n\n").lower()
        if play not in ["yes", "y", "n", "no"]:
            play = input("Please Enter: yes or no, [y/n]")
        if play == "y":
            continue
        else:
            break

if __name__ == "__main__":
    Game()