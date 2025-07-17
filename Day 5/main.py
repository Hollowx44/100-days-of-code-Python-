import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_list=""
for alphabet in range(1,nr_letters+1):
    choosen_letter=random.choice(letters)
    pass_list+=choosen_letter
print(pass_list)

for number in range(1,nr_numbers+1):
    choosen_number=random.choice(numbers)
    pass_list+=str(choosen_number)
print(pass_list)

for symbol in range(1,nr_symbols+1):
    choosen_symbol=random.choice(symbols)
    pass_list+=str(choosen_symbol)
print(pass_list)

password=list(pass_list)
random.shuffle(password)
print(password)

final_pass=''.join(password)

print(f"Your password is:{final_pass}")