from data import question_data
from random import shuffle


class Question:
    def __init__(self, q_text: str, q_answer: str):
        self.text = q_text
        self.answer = q_answer


class QuizBrain:
    def __init__(self):
        self.question_number = 0
        self.question_list = [Question(i["text"], i["answer"]) for i in question_data]
        shuffle(self.question_list)
        self.score = 0

    def next_question(self):
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {next_question.text} (True/False)?: ").title()
        while u_answer not in ["True", "T", "False", "F"]:
            print("Mismatched input. Type 'T'/'True' for True or 'F'/'False' for False")
            u_answer = input(f"Q.{self.question_number}: {next_question.text} (True/False)?: ").title()
        u_answer = "True" if u_answer == "T" else "False"
        if self.check_answer(next_question.answer, u_answer):
            self.score += 1
            print("You got it right!")
        else:
            print("You were wrong!")
        if self.game_is_on():
            print("Next question is:")

    def check_answer(self, correct_answer, user_answer):
        print(f"The correct answer is {correct_answer}")
        return correct_answer == user_answer

    def game_is_on(self):
        return len(self.question_list) > self.question_number
