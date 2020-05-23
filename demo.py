#Simplest basic version of blackjack just to practice
#Note1 - It doesn't take into account the duality of the Ace or 1, thus blackjack is not happening (SOLVED)
#Note2 - Only one game can be played at a time
#Note3 - Players are limited to variable creation
#Note4 - No system of proper strorage of data
#Note5 - points are used instead of using cards
#Note6 - Pretty much a real ineffecient code in general
#TEST CODE WITH JUST A SINGLE PLAYER

import random

points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#Total Points and 1 is also 11

game_on = True

def add_points(array):
    points = 0
    for items in array:
        points += items
    return points

while game_on: #while the game is not over

    #1st round: dealer gives a card to the player

    dealer = []
    player = []

    player_points = 0
    player_points_total = 0
    dealer_points = 0

    initial_rounds = 2

    for round in range(initial_rounds):
        player.append(random.randint(1, 10))
        dealer.append(random.randint(1, 10))

    print(player)
    print(dealer[0])

    if 1 in player:
        if add_points(player) + 10 == 21: #Since 1 = Ace so [1/Ace , 10/King,Queen,J] = 11 so we add 10 with add_points to check if its a blackjack
            print("Player Wins BLACKJACK!!")
            break
    else:
        input = input("Hit or pass")
        if input == "H": #Hit or passH or passP (Correct) / Hit or pass H or pass P(wrong) while testing
            player.append(random.randint(1, 10))
            if add_points(player) > 21:
                print(f"Player Lost, Player: {add_points(player)}, Dealer: {add_points(dealer)} 1 {player},{dealer}")
                break
            elif input == "P":
                pass
        if add_points(dealer) < 17:
            dealer.append(random.randint(1, 10))
            if add_points(dealer) > 21:
                print(f"Player Wins, Player: {add_points(player)}, Dealer: {add_points(dealer)} 2 {player},{dealer}")
                break
            else:
                if add_points(player) > add_points(dealer):
                    print(f"Player Wins, Player: {add_points(player)}, Dealer: {add_points(dealer)} 3 {player},{dealer}")
                    break
                elif add_points(player) == add_points(dealer):
                    print(f"Game Tied, Player: {add_points(player)}, Dealer: {add_points(dealer)} 4 {player},{dealer}")
                    break
                else:
                    print(f"Player Lost, Player: {add_points(player)}, Dealer: {add_points(dealer)} 5 {player},{dealer}")
                    break
        else:
            if add_points(player) > add_points(dealer):
                print(f"Player Wins, Player: {add_points(player)}, Dealer: {add_points(dealer)} 6 {player},{dealer}")
                break
            elif add_points(player) == add_points(dealer):
                print(f"Game Tied, Player: {add_points(player)}, Dealer: {add_points(dealer)} 7 {player},{dealer}")
                break
            else:
                print(f"Player Lost, Player: {add_points(player)}, Dealer: {add_points(dealer)} 8 {player},{dealer}")
                break
    game_on = False
