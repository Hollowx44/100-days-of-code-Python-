#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    with open("./Input/Names/invited_names.txt") as names:
        letter_final=letter.read()
        invited_name=names.readlines()
        for i in range(len(invited_name)):
            with open(f"/home/kukki/Documents/100 Days of code --git/100-days-of-code-Python-/Day24/Mail Merge Project/Output/ReadyToSend/letter_for_{invited_name[i]}.txt",'w') as letter_with_names:
                letter_with_names.write(letter_final.replace("[name]",invited_name[i].rstrip("\n")))
                #print(letter_with_names)
