#ATTRIBUTES:    question_number =0 will keep track,
#               question_list
#METHOD:         next_question()
class Quiz_Brain :
    def __init__(self , q_list):
        self.question_number = 0        #question no would be stored here
        self.question_list = q_list     #array of all the q_no
        self.score = 0

# TO DO - asking the question
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        global user_answer
        user_answer = input(f"Q.{self.question_number}] {current_question.text} (True / False):  ")
        self.check_answer(user_answer,current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

#TO DO - checking if the answer is right
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower() :
            self.score += 1
            print("You're absolutely correct👍")
        else:
            print(f"Oops, that's incorrect!")
        print(f"The correct answer would be {correct_answer}")
        print(f"Your current score is: {self.score} / {self.question_number}")
#TO DO - checking if we're at the end of the quiz








