from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
BACK_BG_COLOR = "#85C7AD"

window=Tk()
window.title("Hollowx44")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#------------------------------------Word selector------------------------------------#
try:
    data=pandas.read_csv("words_to_learn.csv")
    words_data=data.to_dict(orient="records")

except:
    data=pandas.read_csv("japanese_words.csv")
    words_data=data.to_dict(orient="records")

def word_selector():
    global choice, flip_word
    window.after_cancel(flip_word)
    canvas.itemconfig(canvas_image,image=jpy_bg)
    choice=random.choice(words_data)
    language.config(text="Japanese",bg="white",highlightthickness=0)
    word.config(text=choice["Japanese"],bg="white",highlightthickness=0)
    flip_word=window.after(3000,flip)

#------------------------------------flip func------------------------------------#
def flip():
    canvas.itemconfig(canvas_image,image=eng_bg)
    word.config(text=choice["English Meaning"],bg=BACK_BG_COLOR,highlightthickness=0)
    language.config(text="English",bg=BACK_BG_COLOR,highlightthickness=0)

def is_known():
    words_data.remove(choice)
    not_known_data=pandas.DataFrame(words_data)
    not_known_data.to_csv("words_to_learn.csv",index=False)
    word_selector()

def reset():
    global words_data
    window.after_cancel(flip_word)
    word.config(text="Press X to Start Fresh",bg=BACK_BG_COLOR,highlightthickness=0)
    language.config(text="Oh!!",bg=BACK_BG_COLOR,highlightthickness=0)
    reset=pandas.read_csv("japanese_words.csv")
    reset.to_csv("words_to_learn.csv",index=False)    
    words_data=reset.to_dict(orient="records")
    
#------------------------------------UI Setup----------------------------------------------------#
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
jpy_bg=PhotoImage(file="card_front.png")
canvas_image=canvas.create_image(400,263,image=jpy_bg)
eng_bg=PhotoImage(file="card_back.png")

canvas.grid(row=0,column=0,columnspan=2)

#------------------------------------Labels------------------------------------#
language=Label(text="Ready to Learn?",font=('Ariel',30,'italic'),bg="white",highlightthickness=0)
word=Label(text="Press any button to start!",font=('Ariel',40,'bold'),bg="white",highlightthickness=0)
credits=Label(text="~Hollowx44",font=('Ariel',12,'bold'),bg=BACKGROUND_COLOR,highlightthickness=0)

#Griding Label
language.place(x=400,y=150,anchor='center')
word.place(x=400,y=263,anchor='center')
credits.place(x=400,y=550,anchor='center')

#------------------------------------Buttons------------------------------------#
known_logo=PhotoImage(file="right.png")
known=Button(image=known_logo,highlightthickness=0,command=is_known)
not_known_logo=PhotoImage(file="wrong.png")
not_known=Button(image=not_known_logo,highlightthickness=0,command=word_selector)
reset=Button(text="Reset",bg=BACKGROUND_COLOR,font="bold",command=reset)

#Griding Buttons
known.grid(row=1,column=0)
not_known.grid(row=1,column=1)
reset.place(x=400,y=600,anchor='center')

flip_word=NONE
word_selector()

window.mainloop()