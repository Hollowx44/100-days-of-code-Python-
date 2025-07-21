import art
import random
def number_game():
    print(art.logo)
    print("Guess the secret number between 1 and 100 (;_;) ----> [1 and 100 are inclusive]")
    num=random.randint(1,100)
    level=input("Pick your poison! --> (Strong/Light): ").lower()
    if level == "strong":
        chances = 5
    elif level == "light":
        chances = 10
    else:
        print("Pssst!")
        return
    print(f"LVL: {level} poison".title())
    while chances > 0:
        guess=int(input("Your Guess: "))
        if guess > num:
            print("Too High!")
        elif guess < num:
            print("Too Low")
        else:
            print(f"{art.win}\nCongratulations the correct answer was {num}")
            return
        chances -= 1
        print(f"Remaining chances: {chances}")
    print(f"{art.lose}\nTHE SECRET NUMBER WAS: {num}")
    return
number_game()