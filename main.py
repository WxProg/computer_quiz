from logo import header_logo
from question_model import Question
from data import question_data
from quiz_brain import QuizMaster


def computer_quiz():
    question_bin = []

    for question in question_data:
        question_text = question['question']
        question_correct_answer = question['correct_answer']
        question_incorrect_answers = question['incorrect_answers']
        new_question = Question(question_text, question_correct_answer, question_incorrect_answers)
        question_bin.append(new_question)

    quiz = QuizMaster(question_bin)
    print(header_logo)
    print("Guess the riddle and then attempt the quiz.\nThe answer to the riddle will "
          "be displayed at the end of the quiz.")
    print("!!!GOOD LUCK!!!")

    print("\nRiddle: I’m your “waiter” for information. What I am?\n".upper())

    while quiz.quizzing():
        quiz.next_question()
    print("The quiz has concluded.")
    print(f"Your final score stands at: {quiz.score}/{quiz.question_number}")
    print("\nThe answer to the riddle is: 'A server!'")


computer_quiz()
