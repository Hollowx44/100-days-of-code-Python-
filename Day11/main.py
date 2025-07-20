import random
def BlackJack():
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
    print(f"Player's Hand: {p_cards}  ||  Dealer's Hand: {d_cards}\nPlayer's Score: {player_sum}\n")
    while p_choice:
        way = input('"Y" for Hit  ||  "N" for Stand\nPLayer Chose:').lower()
        if way == 'y':
            p_data = random.choice(cards)
            p_cards.append(p_data)
            player_sum += p_data
            print(f"Player Card: {p_data}   ||  Player's Hand: {p_cards}  ||  Player's Score: {player_sum}\n")
            if player_sum > 21:
                print('You loose')
                return
            elif player_sum == 21:
                print('BLACKJACK ----> You Win')
                return

        elif way == 'n':
            print('Player chose Stand\n')
            p_choice = False

    d_choice = True
    while d_choice:
        d_data = random.choice(cards)
        d_cards.append(d_data)
        dealer_sum += d_data
        if dealer_sum > 21:
            print(f"Dealer loose -----> Dealer's Score: {dealer_sum}")
            return
        elif dealer_sum==21:
            print(f"BLACKJACK ---> Dealer win ----> Dealer's score: {dealer_sum}")
            return
        elif dealer_sum >= 17:
            print(f"Dealer on Stand  || Dealer's Hand: {d_cards}  ||  Dealer's Score: {dealer_sum}\n")
            d_choice = False

    if dealer_sum == player_sum:
        print("DRAW!!")
    elif dealer_sum > player_sum:
        print(f"Dealer Win -----> Player's Score: {player_sum}")
    else:
        print(f"Player Win ------> Player's Score: {player_sum}")
while True:
    choice=input("Want to play a game of BlackJack (Y/N): ").lower()
    if choice == "y":
        BlackJack()
    elif choice == "n":
        break
    else:
        print("Enter valid choice!!")