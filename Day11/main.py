import random
def endgame():
    while True:
        pass
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_sum = 0
player_sum = 0
p_cards = []
d_cards = []
d_data = random.choice(cards)
d_cards.append(d_data)
dealer_sum += d_data
for i in range(2):
    p_data = random.choice(cards)
    p_cards.append(p_data)
    player_sum += p_data
p_choice = True
print(f"Player's Hand: {p_cards}  ||  Dealer's Hand: {d_cards}")
while p_choice:
    way = input('Y for Hit  ||  N for Stand\nPLayer Chose:').lower()
    if way == 'y':
        p_data = random.choice(cards)
        p_cards.append(p_data)
        player_sum += p_data
        print(f"Player Card: {p_data}   ||  Player's Hand: {p_cards} ")
        if player_sum > 21:
            print('You loose')
            endgame()
        elif player_sum == 21:
            print('BLACKJACK ----> You Win')
            endgame()

    elif way == 'n':
        print('Player chose Stand')
        p_choice = False

d_choice = True
while d_choice:
    d_data = random.choice(cards)
    d_cards.append(d_data)
    dealer_sum += d_data
    print("Dealer on Hit")
    print(f"Dealer Card: {d_data}   ||  Dealer's Hand: {d_cards} ")
    if dealer_sum > 21:
        print("Dealer loose")
        endgame()
    elif dealer_sum==21:
        print("BLACKJACK ---> Dealer win")
        endgame()
    elif dealer_sum >= 17:
        print("Dealer on Stand")
        d_choice = False

if dealer_sum == player_sum:
    print("DRAW!!")
elif dealer_sum > player_sum:
    print("Dealer Win")
else:
    print("Player Win")