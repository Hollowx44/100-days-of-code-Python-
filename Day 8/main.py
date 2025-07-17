def caesar(orignal_text,shift_amt,direction):
    if direction == "encode": 
        encrypted_text=""
        for letter in orignal_text:
            if letter in alphabet:
                position=alphabet.index(letter)
                encrypted_text +=alphabet[(position+shift_amt)%len(alphabet)]
            else:
                 encrypted_text +=letter
        print(f"Here is the encrypted text you asked:        {encrypted_text}")
        return
    elif direction == "decode":
        decrypted_text=""
        for letter in orignal_text:
            if letter in alphabet:
                position=alphabet.index(letter)
                decrypted_text +=alphabet[(position-shift_amt)%len(alphabet)]
            else:
                decrypted_text += letter
        print(f"Here is fhe decrpyted text you asked:     shift of {shift_amt}   {decrypted_text}")
        return
    
    else:
        print("Error! Choose the correct instruction")
        return
  
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run_again="True"
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    if direction == "decode":
        way=input("Do you know the shift value? yes/no?\n").lower()
        if way == "yes":
            shift = int(input("Type the shift number:\n"))
            caesar(text,shift,direction)
        elif way == "no":
            for i in range(26):
                caesar(text,i,direction)
    else:
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
    choice=input("Wanna Go Again, Yes/No?\n").lower()
    if choice == "yes":
        print("Welcome to Caesar cipher again!")
    elif choice == "no":
        break