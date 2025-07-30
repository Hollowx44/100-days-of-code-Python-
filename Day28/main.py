from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


window=Tk()
window.title("Pomodora")
window.config(bg=YELLOW)

reps=0
checks=0
timer=""
# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text=("00:00"))
    label_status.config(text="Ready?",fg="brown")
    label_checks.config(text="")
    global checks
    checks=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps in (0,2,4,6):
        label_status.config(text="Grind!!",fg=GREEN)
        countdown(WORK_MIN*60)
    elif reps in (1,3,5):
        label_status.config(text="Break",fg=PINK)
        countdown(SHORT_BREAK_MIN*60)
    elif reps==7:
        label_status.config(text="Now Rest:)",fg=RED)
        countdown(LONG_BREAK_MIN*60)
    else:
        return
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global checks
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=(f"0{count_sec}")
    if count>=0:
        canvas.itemconfig(timer_text,text=(f"{count_min}:{count_sec}"))
        global timer
        timer=window.after(1000,countdown,count-1)

    if count==0:
        reps+=1
        if reps%2!=0:
            checks+=1
            label_checks.config(text="✔"*checks)
        start_timer()    
# ---------------------------- UI SETUP ------------------------------- #

canvas=Canvas(width=500,height=500,bg=YELLOW,highlightthickness=0)
imageT=PhotoImage(file="tomato_chan.png")
canvas.create_image(250,250,image=imageT)
timer_text=canvas.create_text(225,340,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(row=2,column=2)


#label
label_credits=Label(text="-Hollowx44",bg=YELLOW,font=(FONT_NAME,10,"italic"))
label_checks=Label(text="",bg=YELLOW,fg=GREEN,font=(FONT_NAME,30,"bold"))
label_status=Label(text="Ready?",bg=YELLOW,fg="brown",font=(FONT_NAME,20,"bold"))

#label1.grid(row=1,column=2)
label_credits.grid(row=10,column=2)
label_checks.grid(row=3,column=2)
label_status.place(x=450,y=220)
#button
st_button=Button(text="Start",command=start_timer)
reset_button=Button(text="Reset",command=timer_reset)

st_button.grid(row=3,column=1)
reset_button.grid(row=3,column=3)


window.mainloop()