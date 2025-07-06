import random
import sys

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
continue_game = True

def start_game():
    player_cards = []
    dealer_cards = []
    sum=0
    for i in range(0,2):
        player_cards.append(random.choice(cards))
        if i==1 and player_cards[i]==11:
            chose_which_one = input(f"Your Cards are {player_cards} Would you like to consider it as 11 or 1: ")
            if chose_which_one==1:
                sum += 1
            elif chose_which_one==11:
                sum += 11
        sum+=player_cards[i]
    dealer_cards.append (random.choice(cards))
    cont_player (player_cards,dealer_cards, sum)

def cont_player(player_cards,dealer_cards,sum):
    check_twenty_0ne(sum)
    print(f"The Player card is: {player_cards} and your sum is: {sum}")
    print(f"Dealer card is: {dealer_cards}")
    contunue_choice = input("Type 'y' if you want another card or 'n' if you want to stop:")
    if contunue_choice == 'y':
        player_cards.append(random.choice(cards))
        sum+=player_cards[-1]
        check_twenty_0ne(sum)
        cont_player(player_cards,dealer_cards,sum)
    if contunue_choice == 'n':
        check_twenty_0ne(sum)
        cont_dealer(player_cards,dealer_cards,sum)

def check_twenty_0ne(sum):
    if sum == 21:
        print(f"Congratulations! You Win with {sum} points")
        new_game()
    if sum > 21:
        print(f"You Lost with {sum} points")
        new_game()



def cont_dealer(player_cards,dealer_cards,sum):
    sum_dealer=0
    print(dealer_cards)
    while sum_dealer<17:
        dealer_cards.append (random.choice(cards))
        print(dealer_cards)
        sum_dealer = dealer_cards[-1] + sum_dealer
    if sum_dealer > 21:
        print(f"The dealer sum is: {sum_dealer}, Dealer lost")
        new_game()
    check_result(player_cards,dealer_cards,sum_dealer,sum)
    new_game()

def new_game():
    new_game= input("Would you like to play again? (y/n) : ").lower()
    if new_game == "y":
        start_game()
    sys.exit()


def check_result(player_cards,dealer_cards,sum_dealer,sum) :
    if sum_dealer>sum:
        print(f"The dealer sum is {sum_dealer} and The player sum is {sum}")
        print(f"The dealer Win!")
        return True

    if sum_dealer==sum:
        print(f"The dealer sum is {sum_dealer} and The player sum is {sum}: You Win!")
        return True

    print(f"The dealer sum is {sum_dealer} and The player sum is {sum}")
    print(f"The Player Win!")

start_game()


