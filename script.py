# IMPORTING RANDOM MODULE, AND THE HASHMAP DATA STRUCTURE
# WHICH WE CREATED IN HASHMAPS.PY
import random
from hashmaps import HashMap

# INITIALIZING THE HASHMAP CLASS WITH THE ARRAY SIZE
hash_map = HashMap(13)

hash_map.assign("Ace", 1)  #("Ace", 11) calculated through algorithm
hash_map.assign("Two", 2)
hash_map.assign("Three", 3)
hash_map.assign("Four", 4)
hash_map.assign("Five", 5)
hash_map.assign("Six", 6)
hash_map.assign("Seven", 7)
hash_map.assign("Eight", 8)
hash_map.assign("Nine", 9)
hash_map.assign("Ten", 10)
hash_map.assign("Jack", 10)
hash_map.assign("Queen", 10)
hash_map.assign("King", 10)

# LIST OF CARDS TO BE SELECTED OUT OF

cards = ["Ace", "Twice", "Three", "Four",
         "Five", "Six", "Seven", "Eight",
         "Nine", "Ten", "Jack", "Queen",
         "King"]

game_on = True

while game_on:

    # GAME FUNCTIONS
    def points(array):
        total_points = 0
        for card_name in array:
            total_points += hash_map.retrieve(card_name)
        return total_points

    def print_cards(array_name, array):
        print(array_name, array)

    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(cards[random.randint(0, 12)])
        dealer_cards.append(cards[random.randint(0, 12)])

    print_cards("Player: ", player_cards)
    print_cards("Dealer: ", dealer_cards[0])

    win = "PLAYER WINS"
    lost = "PLAYER LOST"
    tied = "GAME TIED"

    # CHECK FOR BLACKJACK
    if "Ace" in player_cards:
        if points(player_cards) + 10 == 21:
            print("Player Wins, BLACKJACK!!")
            break

    # IF BLACKJACK DIDN'T HAPPEN
    user_input = input("Hit or pass")
    if user_input == " H":
        player_cards.append(cards[random.randint(0, 12)])
        if points(player_cards) > 21:
            print(lost)
            print_cards("Player: ", player_cards)
            print_cards("Dealer: ", dealer_cards)
            break

    # CHECK IF DEALER'S CARDS TOTAL TO LESS THAN 17
    if points(dealer_cards) < 17:
        dealer_cards.append(cards[random.randint(1, 10)])
        if points(dealer_cards) > 21 or points(player_cards) > points(dealer_cards):
            print(win)
            print_cards("Player: ", player_cards)
            print_cards("Dealer: ", dealer_cards)
            break
        elif points(player_cards) == points(dealer_cards):
            print(tied)
            print_cards("Player: ", player_cards)
            print_cards("Dealer: ", dealer_cards)
            break
        elif points(player_cards) < points(dealer_cards):
            print(lost)
            print_cards("Player: ", player_cards)
            print_cards("Dealer: ", dealer_cards)
            break

    # IF DEALER'S CARDS ARE NOT LESS THAN 17
    if points(player_cards) > points(dealer_cards):
        print(win)
        print_cards("Player: ", player_cards)
        print_cards("Dealer: ", dealer_cards)
        break
    elif points(player_cards) == points(dealer_cards):
        print(tied)
        print_cards("Player: ", player_cards)
        print_cards("Dealer: ", dealer_cards)
        break

    print(lost)
    print_cards("Player: ", player_cards)
    print_cards("Dealer: ", dealer_cards)




    game_on = False

# GAME DONE