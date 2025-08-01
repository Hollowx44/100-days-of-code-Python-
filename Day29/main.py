from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for x in range(nr_letters)]
    password_symbols = [random.choice(symbols) for x in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for x in range(nr_numbers)]

    password_list=password_letters+password_numbers+password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():    
    website=website_input.get()
    emailusername=emailusername_input.get()
    password=pass_input.get()
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="INPUT ERROR",message="Don't leave any field empty!!")
    else:
        pop_up=messagebox.askokcancel(title=website,message=f"These are your entered details: \nEmail:{emailusername}\nPassword:{password}")
        if pop_up==True:
            with open("login_data.txt","a") as secret_stash:
                secret_stash.write(f"{website} | {emailusername} | {password} \n")
                #Delete functionality
                website_input.delete(0,END)
                pass_input.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=0)
image_logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image_logo)
canvas.grid(row=0,column=1)

#labels
website_label=Label(text="Website:")
emailusername_label=Label(text="Email/Username:")
pass_label=Label(text="Password:")


#griding lables
pass_label.grid(row=3,column=0)
emailusername_label.grid(row=2,column=0)
website_label.grid(row=1,column=0)

#buttons
genrator_button=Button(text="Generate Password",width=12,command=generate_password)
add_button=Button(text="Add",width=36,command=save)

#griding buttons
genrator_button.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)

#Inputs
pass_input=Entry(width=24)
website_input=Entry(width=35,font=23)
website_input.focus()
emailusername_input=Entry(width=35,font=23)
emailusername_input.insert(0,"hollowx44@gmail.com")

#Griding Inputs
pass_input.grid(row=3,column=1)
website_input.grid(row=1,column=1,columnspan=2)
emailusername_input.grid(row=2,column=1,columnspan=2)
window.mainloop()