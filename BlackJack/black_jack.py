import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_cards = []

def cont():
    continue_game = True
    while continue_game:
        continue_game = input("Type 'y' if you want another card or 'n' if you want to stop:")


def start_game():
    sum=0
    for i in range(0,2):
        player_cards.append(random.choice(cards))
        sum+=player_cards[i]
    print(f"Your Cards are: {player_cards}")
    print(sum)
    if sum>21:
        print(f"The sum is: {sum}, You lost")
    else:
        dealer_card = random.choice(cards)
        print(f"Dealer card is: {dealer_card}")
        return dealer_card


start_game()
print(sum)
