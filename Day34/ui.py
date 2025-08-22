from tkinter import *
from quiz_brain import QuizBrain
# from main import quiz
THEME_COLOR = "#375362"

class Aniquiz:
    def __init__(self,quiz):
        self.quiz=quiz
        self.windows=Tk()
        self.windows.title("Anime quiz")
        self.windows.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas=Canvas(height=250,width=300)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        #Label
        self.quiz_question=self.canvas.create_text(150,120,text="HI WEEBS",width=250,font=("Arial",20,"italic"))
        self.score_logo=Label(text="Score:0",bg=THEME_COLOR,fg="white")
        #griding logo
        # self.quiz_question.grid(row=1,column=0,columnspan=2)
        self.score_logo.grid(row=0,column=1)
        #Buttons
        true_logo=PhotoImage(file="/Day34/images/true.png")
        self.true=Button(image=true_logo,highlightthickness=0,command=lambda:self.answer_evalation("True"))
        false_logo=PhotoImage(file="/Day34/images/false.png")
        self.false=Button(image=false_logo,highlightthickness=0,command=lambda:self.answer_evalation("False"))
        #griding buttons
        self.true.grid(row=2,column=0)
        self.false.grid(row=2,column=1)
        self.get_question()
        self.windows.mainloop()

        #next_question
    def get_question(self):
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.quiz_question,text=q_text)
    def answer_evalation(self,user_answer):
        out=self.quiz.check_answer(user_answer)
        self.score_logo.config(text=f"Score:{self.quiz.score}")
        self.give_feedback(out)
        if self.quiz.still_has_questions() == True:
            self.windows.after(1000,self.get_question)
           
        else:
            self.windows.after(1000,lambda:self.canvas.itemconfig(self.quiz_question,text="You've completed the quiz.....congrats!"))
            self.windows.after(1000,lambda:self.canvas.config(bg="white"))
            self.true.config(command=NONE)
            self.false.config(command=NONE)
    def give_feedback(self,color):
        self.canvas.config(bg=color)
        