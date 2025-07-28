import pandas

nato=pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict={row.letter:row.code for (index,row) in nato.iterrows()}

user_word=input("Enter a word:").upper()
user_input_in_phoneticput_nato_form=[word for (letter,word) in phonetic_dict.items() if letter in user_word]
print(user_input_in_phoneticput_nato_form)
