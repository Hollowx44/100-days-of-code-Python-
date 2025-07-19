import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
random_no=random.randint(0,2)
user_input=int(input("ROCK:0    PAPER:1    SCISSORS:2\n Your Choice:"))

print(game_images[user_input])

print("Computer Choice:\n",game_images[random_no])

if random_no==0:
    if user_input==0:
        print("Tie")
    elif user_input==1:
        print("You Win")
    else:
        print("Computer Wins")

if random_no==1:
    if user_input==0:
        print("Computer win")
    elif user_input==1:
        print("Tie")
    else:
        print("You Win")

if random_no==2:
    if user_input==0:
        print("You Win")
    elif user_input==1:
        print("Computer Win")
    else:
        print("Tie")