import data
from select_question import Quiz
from verify_answer import AnswerChecker

quiz = Quiz()

while quiz.asked_question < min(12, len(data.question_data)):  # Garante até 12 perguntas
    user_answer, question_index = quiz.get_question()

    if user_answer is None:  # Se não houver mais perguntas, sai do loop
        break

    verify = AnswerChecker(user_answer, question_index)
    
    is_correct = verify.check_answer()
    
    quiz.update_score(is_correct)
    
    quiz.show_score()

quiz.show_final_score()
