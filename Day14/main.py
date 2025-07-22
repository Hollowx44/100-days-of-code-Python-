from gamedata import data
from art import logo,vs
import random
def pick():
    return random.choice(data)
def Higher_or_Lower():
    state=True
    score=0
    b=pick()
    while state:
        print("\n"*20)
        print(logo)
        def True_answer():
            if a['follower_count'] > b['follower_count']:
                return "a"
            elif a['follower_count'] < b['follower_count']:
                return "b"
        a=b
        b=pick()
        print(logo)
        while a == b:
            b=pick()
        print(f"Compare A: {a['name'], a['description'], a['country']}")
        print(vs)
        print(f"Against B: {b['name'], b['description'], b['country']}")
        guess=input("Who has more followers?  Type 'A' or 'B' ").lower()
        answer=True_answer()
        print(answer)
        if guess==answer:
            score +=1
            print(f"You're Right. Current score {score}")
        elif guess!=answer:
            print(f"Game Over. Your Score {score}")
            return
    
Higher_or_Lower()