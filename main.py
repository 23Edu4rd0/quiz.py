from select_question import Quiz
from verify_answer import AnswerChecker

quiz = Quiz()

while quiz.asked_question < 10:
    #get the question and the user answer
    user_answer = quiz.get_question()
    
    #create object verify that sees if the answer is correct or not
    verify = AnswerChecker(user_answer,quiz.number_of_question)
    
    # verify if the answer is correct
    is_correct = verify.check_answer()
    
    # if the answer is correct add to the score
    quiz.update_score(is_correct)
    
    #show the score to the player
    quiz.show_score()

final = quiz.show_final_score()
