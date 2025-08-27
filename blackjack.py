"""Blackjack or 21 card game
The classic game also known as 21.
Tags: large, game, card games"""

#Imports---------------------------------
import random, sys

#Constants/Variables--------------------------
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
# ( a list of chr codes unicode above for card signs.)
BACKSIDE = 'backside'

#Functions------------------------------------

#Main execution function===================
def main():
    print("""Blackjack
          
    Rules:
          Try to get as close to 21 without going over.
          Kings, Queen, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking their cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.""")
    
    money = 5000
    while True: #main game loop.
        #Check if player has run out of money.
        if money < 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print("Thanks for playing!")
            sys.exit()
        
        #Let the player enter their bet for this round:
        print("Money: ", money)
        bet = getBet(money)

        #Give dealer and player two cards from the deck each: 
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        #Handle player actions: 
        