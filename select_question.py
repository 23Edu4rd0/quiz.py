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
        # Sees if the question number is on the list
        if self.number_of_question not in self.number_list:
            # Add a value that is show every question done
            self.asked_question += 1
            # Show the question
            answer = input(f"{self.asked_question}: {question_data[self.number_of_question]["question"]} (True/False): ").lower()
            #Add the number in a list, so the question can't show it again
            self.number_list.append(self.number_of_question)
            return answer
        
        else:
            while self.number_of_question in self.number_list:
                #Create a new number until this number is not in the list
                self.number_of_question =  random.randrange(0,len(question_data))
            return self.get_question()
            
    
    
    def update_score(self, is_correct):
        #module that add a point to score, so can show if is right or wrong
        if is_correct:
            self.score += 1
    
     #shows the current score and the final question, maybe i could create a object for that
    def show_score(self):
        print(f"Your current score is: {self.score}\n ")
    
    def show_final_score(self):
        clear_screen()
        print(f"\nYou've completed the quiz\nYour final score was {self.score}/10")