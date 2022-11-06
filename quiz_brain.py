# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz

class QuizMaster:

    def __init__(self, ques_list):
        self.score = 0
        self.question_number = 0
        self.ques_list = ques_list

    def quizzing(self):
        ques_length = len(self.ques_list)
        return ques_length > self.question_number

    def next_question(self):
        current_question = self.ques_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} {current_question.text}"
                            f"\n{current_question.incorrect_answer}: ").lower()
        self.check_answer(user_answer, current_question.correct_answer)

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("That's indeed correct. Let's Goo!")
        else:
            self.score -= 1
            print("That's wrong my friend. However, keep going. You got this!")
            print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

