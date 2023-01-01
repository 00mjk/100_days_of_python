class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list 
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1 
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.questions_list) 

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower(): 
            print("You got it right!")
            self.score += 1     
        else: 
            print("That's wrong!") 

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score {self.score}/{self.question_number}.\n")
    
    