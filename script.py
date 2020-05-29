# Importing the random module
import random

# Assigning the cards to their values
card_deck = {'Ace': 1, 'Twice': 2, 'Thrice': 3,
             'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
             'Eight': 8, 'Nine': 9, 'Ten': 10,
             'Jack': 10, 'Queen': 10, 'King': 10}

# The cards list from which the cards will be distributed
cards = ['Ace', 'Twice', 'Thrice',
         'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King']


# Function for calculating the total points of the cards in hand
def points(array):
    total_points = 0
    for card_name in array:
        total_points += card_deck[card_name]
    return total_points


# viewing player and dealer cards
def view_cards(player, dealer):
    print(f"Player: {player},\n"
          f"Dealer: {dealer}")


# Player cards and Dealer cards
player_cards = []
dealer_cards = []

# Distributing the two initial cards
for _ in range(2):
    player_cards.append(cards[random.randint(0, 12)])
    dealer_cards.append(cards[random.randint(0, 12)])

# Showing the cards
print(f"Player: {player_cards}")
print(f"Dealer: {dealer_cards[0]}")

# If the player has an Ace and a ten pointer [BLACKJACK]
if "Ace" in player_cards:
    if points(player_cards) + 10 == 21:
        print("Player Wins, BLACKJACK!!\n")

# If player doesn't have a blackjack
else:
    enter_input = input("Do you want to Hit or Pass(y/n):")

    # the player can get cards while he presses y and hits
    while enter_input == "y":
        player_cards.append(cards[random.randint(0, 12)])
        print(player_cards)

        # to check if the total points of his cards is more than 21
        if points(player_cards) > 21:
            print("PLAYER LOST")
            print(player_cards)
            break
        enter_input = input("Do you want to Hit or Pass(y/n):")

    # if the player presses p and passes
    if enter_input == 'n':

        # to check if dealer cards equal less than 17
        if points(dealer_cards) < 17:
            dealer_cards.append(cards[random.randint(0, 12)])

        # to check if dealer points is more than 21 Or
        # player points is more than the dealer
        if points(dealer_cards) > 21 or points(player_cards) > points(dealer_cards):
            print("PLAYER WINS")
            view_cards(player_cards, dealer_cards)

        # to check if game is tied and dealer and player has same points
        elif points(player_cards) == points(dealer_cards):
            print("GAME TIED")
            view_cards(player_cards, dealer_cards)

        # to check if dealer has more points than player
        else:
            print("PLAYER LOST")
            view_cards(player_cards, dealer_cards)
            
# GMAE COMPLETE
