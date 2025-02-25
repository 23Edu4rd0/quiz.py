from data import question_data

class AnswerChecker:
    def __init__(self,answer, question_index):
        self.user_response = answer
        self.question_index = question_index
        self.correct_option = question_data[self.question_index]["correct_answer"].lower()
        
    def check_answer(self):
        if self.user_response == self.correct_option:
            print(f"You got it right!")
            return True
        else:
            print(f"That's wrong.\nThe corret answer was: {self.correct_option}")
            return False
        
    