
with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names:
        letter_final=letter.read()
        invited_name=names.readlines()
        for i in range(len(invited_name)):
            with open(f"/home/kukki/Documents/100 Days of code --git/100-days-of-code-Python-/Day24/Mail Merge Project/Output/ReadyToSend/letter_for_{invited_name[i]}.txt",'w') as letter_with_names:
                letter_with_names.write(letter_final.replace("[name]",invited_name[i].rstrip("\n")))
                #print(letter_with_names)
