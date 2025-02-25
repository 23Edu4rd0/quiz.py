from data import question_data
import random
import os

def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

class Quiz:
    def __init__(self):
        self.number_of_question = random.randrange(0, len(question_data))
        self.number_list = []
        self.asked_question = 0
        self.score = 0 

    
    
    def get_question(self):
        if self.number_of_question not in self.number_list:
            self.asked_question += 1
            answer = input(f"{self.asked_question}: {question_data[self.number_of_question]["question"]} (True/False): ").lower()
            self.number_list.append(self.number_of_question)
            return answer
        else:
            while self.number_of_question in self.number_list:
                self.number_of_question =  random.randrange(0,len(question_data))
            return self.get_question()
            
    
    
    def update_score(self, is_correct):
        if is_correct:
            self.score += 1
    
    def show_score(self):
        print(f"Your current score is: {self.score}\n ")
    
    def show_final_score(self):
        clear_screen()
        print(f"\nYou've completed the quiz\nYour final score was {self.score}/10")