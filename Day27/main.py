from tkinter import *

window=Tk()
window.title("Mile to Km Converter")
#window.minsize(width=250,height=130)
window.config(padx=20,pady=20)

#defining function
def miles_to_km():
    miles=input.get()
    km = round(float(miles)*1.609,2)
    lable4.config(text=str(km))

#lables
lable1=Label(text="Miles",font=10)
lable2=Label(text="is equal to",font=10)
lable3=Label(text="Km",font=10)
lable4=Label(text="0",font=10)
#griding labels
lable1.grid(row=1,column=3)
lable2.grid(row=2,column=1)
lable3.grid(row=2,column=3)
lable4.grid(row=2,column=2)
#button
button1=Button(text="Calculate",command=miles_to_km)
button1.grid(row=3,column=2)

#input
input=Entry(width=10,font=10)
input.insert(END,string="0")
input.grid(row=1,column=2)

window.mainloop()