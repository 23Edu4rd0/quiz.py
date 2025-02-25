from data import question_data
import random
import os

class Quiz:
    def __init__(self):
        self.number_list = random.sample(range(len(question_data)), len(question_data))
        self.asked_question = 0
        self.score = 0 

    
    def get_question(self):
        if self.asked_question < len(question_data):  # Garante que ainda há perguntas para fazer
            question_index = self.number_list[self.asked_question]  # Pega a próxima pergunta da lista embaralhada
            self.asked_question += 1
            return input(f"{self.asked_question}: {question_data[question_index]['question']} (True/False): ").lower(), question_index
        else:
            return None, None
            
    
    
    def update_score(self, is_correct):
        #module that add a point to score, so can show if is right or wrong
        if is_correct:
            self.score += 1
    
     #shows the current score and the final question, maybe i could create a object for that
    def show_score(self):
        print(f"Your current score is: {self.score}\nYou got it {self.score}/{self.asked_question}\n ")
    
    def show_final_score(self):
        print(f"\nYou've completed the quiz\nYour final score was {self.score}/{len(question_data)}")