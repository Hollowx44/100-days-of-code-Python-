class QuizBrain:
    def __init__(self,question_list):
        self.question_list=question_list
        self.question_number=0
        self.score = 0
    def still_has_questions(self):
         return self.question_number < len(self.question_list)
    def next_question(self):
            current_question=self.question_list[self.question_number]
            quiz_ans=input(f"Q{self.question_number + 1}: {current_question.text}(True/False)\n")
            self.question_number +=1
            self.check_answer(quiz_ans,current_question.answer)
    def check_answer(self,quiz_answer,real_answer):
         if quiz_answer.lower() == real_answer.lower():
              print("You got it right!")
              self.score += 1
         else:
              print("Wrong answer")
         print(f"The correct answer was {real_answer}")
         print(f"The current score is {self.score}/{self.question_number}")