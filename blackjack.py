import random
import os 
from time import sleep

class Blackjack():
    def __init__(self, card, deck, players_hand, dealers_hand, user_total, dealer_total, game_status):
        self.card = card
        self.deck = deck  
        self.players_hand = players_hand
        self.dealers_hand = dealers_hand
        self.user_total = user_total
        self.dealer_total = dealer_total
        self.game_status = game_status
        self.game_status = {
            'playing': False
        }

# Need to build the deck by adding all possible combinations (ie cards) to it
# Need to also be able to shuffle the deck
# When cards are dealt, they get popped from the deck, and then added back in before shuffling
    def shuffle(self):
        self.deck = []
        self.players_hand = []
        self.dealers_hand = []
        values = range(1,14)
        suits = ["Hearts", "Clubs", "Diamonds", "Spades"]  
        for suit in suits:
            for value in values:
                card = f'{value} of {suit}'
                self.deck.append(card)
        return self.deck

    # Add a card to the dealer's hand
    def dealer_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.dealers_hand.append(card)
        return self.dealers_hand

    # Add a card to the player's hand
    def player_card(self):
        card = random.choice(self.deck)
        self.deck.remove(card)
        self.players_hand.append(card)
        return self.players_hand

    # Add up the user's total
    def check_user_total(self):
        hand_total = []
        for card in self.players_hand:
            card = card.split(" ", -1)
            hand_total.append(int(card[0]))
        self.user_total = sum(hand_total)
        return self.user_total

    # Add up the dealer's total    
    def check_dealer_total(self):
        hand_total = []
        for card in self.dealers_hand:
            card = card.split(" ", -1)
            hand_total.append(int(card[0]))
        self.dealer_total = sum(hand_total)
        return self.dealer_total

    # Report on what the user's hand and total is, wait for 3 seconds, and then report what's showing for the dealer.
    def report_hands(self):
        shown_card = self.dealers_hand[0]
        self.check_user_total()
        self.check_dealer_total()
        print(f"Your hand is: {self.players_hand}\nYour total is: {self.user_total}\n")
        sleep(3)
        print(f"The dealer's card that is showing is the {shown_card}.")
        sleep(2)

    # The user's turn
    # If they have blackjack at the beginning, report on that and skip the rest.
    # If they get to 21, report on that, and skip the rest.
    # If they have gone over 21, report on that and skip the rest.
    def user_hit_or_stand(self):
        if self.user_total == 21 and len(self.players_hand) == 2:
            print('\nYou have Blackjack!')
            sleep(2)
        # elif self.user_total > 21:
        #     return f'You are over 25. You bust.'
        elif self.user_total == 21 and len(self.players_hand) > 2:
            print("\nNice work! You have 21!")
            sleep(2)
        elif self.user_total > 21:
            print("\nYou went over 21.\n")
            sleep(2)
        # For the user's choice, they can add a new card to their hand, and then see their new card and hand.
        # If they stand, report their total.
        # If they have an invalid entry, tell them, and start it over.
        else:
            choice = input("\n\tWould you like to hit or stand? h / s\n")
            if choice.lower() == "h":
                new_card = random.choice(self.deck)
                self.players_hand.append(new_card)
                os.system('clear')
                print(f"You drew the {new_card}.\n")
                sleep(2)
                self.report_hands()
                sleep(2)
                self.user_hit_or_stand()
            elif choice.lower() == "s":    
                os.system('clear')
                print(f"\nYour total is {self.user_total}. Now it's the dealer's turn.\n")
                sleep(2)
            else:
                print("\n\tInvalid input. Please try again.\n")
                sleep(2)
                self.user_hit_or_stand()

    # For the dealer's turn, if they're under 17, add a card. Otherwise, they stay.
    # Need to report on what is happening with the dealer - they drew ___, they're standing, etc.
    def dealers_turn(self):
        total = self.check_dealer_total()
        if total == 21 and len(self.dealers_hand) == 2:
            print("The dealer has Blackjack.")
            sleep(2)
        elif self.user_total > 21:
            print(f"The dealer is standing.\n")
            sleep(2)
        elif total < 17:
            self.dealer_card()
            print(f'\nThe dealer drew a {self.dealers_hand[-1]}.\n')
            sleep(2)
            self.dealers_turn()
        elif 17 <= total <= 21:
            print(f"\nThe dealer is standing.")
            sleep(2)
        elif total > 21:
            print("\nThe dealer went over 21.")
            sleep(2)

    # Reporting on the winner
    def check_for_winner(self):
        os.system('clear')
        print(f"Your hand: {self.players_hand}\n\tYour total: {self.user_total}\n")
        sleep(2)
        print(f"Dealer's hand: {self.dealers_hand}\n\tDealer's total: {self.dealer_total}")
        sleep(2)
        if self.user_total == 21 and len(self.players_hand) == 2:
            print('\nYou have Blackjack! You win!')
            sleep(2)
        elif self.user_total > 21 and self.dealer_total <= 21:
            print("\n\tYou went over 21 and busted. Better luck next time.\n")
        elif self.dealer_total > 21 and self.user_total <= 21:
            print("\n\tYou win! The dealer went over 21.\n")
        elif self.user_total <= 21 and self.dealer_total < self.user_total:
            print(f"\n\tYou win!\n\tYour total is {self.user_total}.\n\tThe dealer has {self.dealer_total}.\n")
        elif self.dealer_total <= 21 and self.dealer_total > self.user_total:
            print(f"\n\tYou lost.\n\tYour total is {self.user_total}.\n\tThe dealer has {self.dealer_total}.\n")
        else:
            print(f"\n\tIt's a push!\n\tYour total is {self.user_total}.\n\tThe dealer has {self.dealer_total}.\n")

    # See if the user wants to play another game or quit
    def keep_playing(self):
        ask = input("Would you like to play again? y/n\n")
        if ask.lower() == "y":
            self.game_status['playing'] = True
            os.system('clear')
        elif ask.lower() == "n":
            self.game_status['playing'] = False
            os.system('clear')
            print("Thanks for playing!\n")

#Instantiate the class
game = Blackjack("card", "deck", [], [], [], [], {})

def play():
    """
    Rules:
1. The game has two players: the Dealer and the Player. The game starts off with a deck of 52 cards. 
The 52 cards consist of 4 different suits: Clubs, Diamonds, Hearts and Spades. For each suit, there are 
cards numbered 1 through 13.

Note: No wildcards are used in the program

2. When the game begins, the dealer shuffles the deck of cards, making them randomized. After the dealer shuffles, 
it will deal the player 2 cards and will deal itself 2 cards. The Player is able to see both of their own 
cards, but only one of the Dealer's cards.

3. The objective of the game is for the Player to count their cards after they're dealt. If they're not satisfied with
 the number, they have the ability to 'Hit'. A hit allows the dealer to deal the Player one additional card. The 
 Player can hit as many times as they'd like as long as they don't 'Bust'. A bust is when the Player is dealt cards 
 that total more than 21.

4. If the dealer deals the Player cards equal to 21 on the first deal, the Player wins. This is referred to as 
Blackjack. Blackjack is NOT the same as getting cards that equal up to 21 after the first deal. Blackjack can only be
 attained on the first deal.

5. The Player will never see the Dealer's hand until the Player chooses to 'stand'. A Stand is when the player tells 
the dealer to not deal it anymore cards. Once the player chooses to Stand, the Player and the Dealer will compare 
their hands. Whoever has the higher number wins. Keep in mind that the Dealer can also bust.
    """

#   Greeting:
    print("\n\tWelcome to Bohnlein's Blackjack Table! Let's play! ")
    sleep(1)
    os.system('clear')

    # Conditional for the game
    game.game_status['playing'] = True
    while game.game_status['playing'] == True:

        # Shuffling, and dealing the cards
        print("Dealer is shuffling...")
        sleep(2)
        os.system('clear')
        print("Dealer is dealing the cards...")
        sleep(2)
        os.system('clear')
        # Cards are dealt, and the cards showing are reported
        game.shuffle()  

        # Player's Hand:
        game.player_card()
        game.player_card()
        
        # Dealer's Hand:
        game.dealer_card()
        game.dealer_card()

        # Report what's in the player's hand and what's showing for the dealer.
        game.report_hands()

        # No winner, so it's the player's turn to hit or stand.
        game.user_hit_or_stand()

        # Dealer's turn. If they have less than 17, they hit. If equal to or more, they stay.
        game.dealers_turn()
        
        # Report on winner
        game.check_for_winner()

        # Continue or stop?
        game.keep_playing()

play()