#simulation.py

from random import random, randrange
print("Hello, welcome to this game of Blackjack")

def main():
    total = 0 
    try:
        gameNo = 1
        busts = 0 
        while total <= 21:
            gameNo = gameNo + 1
            input("Press Enter to draw a card ...")
            card = (randrange(1,14,1))
            if card > 1 and card < 10:
                value = card
                print ("You drew", card)
            if card == 11:
                value = 10
                print("You drew Jack")
            if card == 12:
                value = 10
                print("You drew Queen")
            if card == 13:
                value = 10
                print("You drew King")
            if card == 1:
                value = 11
            if total > 6 and card == 1:
                value = 1
            if card > 13 or card < 1:
                break 
            total = total + value
            print("Your score is now", total)
            if total >= 17 and total < 21:
    #for a non interactive game            print ("Game Over")
                choice = input("Would you like to continue? Yes or No? ")
                if choice == "Yes" or choice == "yes" or choice == "y" or choice == "Y":
                    continue
                if choice == "No" or choice == "no" or choice == "n" or choice == "N":
                    replay = input("Do you want to play again? ")
                    if replay == "Yes" or replay == "yes" or replay == "y" or replay == "Y":
                        main()
                    if replay == "No" or replay == "no" or replay == "n" or replay == "N":
                        quit()
            if total == 21:
                print ("You WON!!!")
                print("your possibility of busting is", (busts/gameNo))
                replay = input("Do you want to play again? ")
                if replay == "Yes" or replay == "yes" or replay == "y" or replay == "Y":
                    main()
                if replay == "No" or replay == "no" or replay == "n" or replay == "N":
                    quit()
                else:
                    quit()
            if total > 21:
                busts = busts + 1
                print ("You crossed 21. Game OVER")
                print("your possibility of busting is", (busts/gameNo))
                replay = input("Do you want to play again? ")
                if replay == "Yes" or replay == "yes" or replay == "y" or replay == "Y":
                    main()
                if replay == "No" or replay == "no" or replay == "n" or replay == "N":
                    quit()
    except:
        UnboundLocalError

        
"""
       elif total < 21 and total >= 17:
            redraw = eval("Would you like to draw again? ")
            if redraw == yes:
                continue
            elif redraw == no:
                print("Game over, your score is", total)
        print (total)
"""
main()
