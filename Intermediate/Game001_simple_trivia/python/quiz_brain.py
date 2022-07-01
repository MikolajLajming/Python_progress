from data import question_data
from random import shuffle


class Question:
    """This class creates object Question\n
    class accepts two variables as it's input.\n
    use: Question(**q_text**, **q_answer**)\n
    Attributes:\n
    **obj.text** = **q_text** -> **str**\n
    Question content\n
    **obj.answer** = **q_answer** -> **str**\n
    Question answer"""
    def __init__(self, q_text: str, q_answer: str):
        self.text = q_text
        self.answer = q_answer


class QuizBrain:
    """This class creates object QuizBrain\n
    class has 2 methods available: next_question() and game_on()\n
    use: Question()\n
    Attributes:\n
    **question_number** -> **int** \n
    The number of question counting from the beginning\n
    **question_list** -> **list** [obj.Question(), obj.Question()...]\n
    list of available objects made with *Question()* class (shuffled)\n
    **score** -> **int**\n
    Number of user points. User gains a point after a correct answer"""
    def __init__(self):
        self.question_number = 0
        self.question_list = [Question(i["text"], i["answer"]) for i in question_data]
        shuffle(self.question_list)
        self.score = 0

    def next_question(self):
        """Prints next question and checks user's answer\n
        Input accepts "True", "T", "False" and "F" as a user input\n
        If anything else typed in, user will be asked to type the answer again\n
        If answer correct, increases user score by 1\n
        Prints if user was right or wrong"""
        next_question = self.question_list[self.question_number]
        self.question_number += 1
        u_answer = input(f"Q.{self.question_number}: {next_question.text} (True/False)?: ").title()
        while u_answer not in ["True", "T", "False", "F"]:
            u_answer = input("Mismatched input. Type 'T'/'True' for True or 'F'/'False' for False").title()
        u_answer = "True" if u_answer == "T" else "False"
        if self.check_answer(next_question.answer, u_answer):
            self.score += 1
            print("You got it right!")
        else:
            print("You were wrong!")
        if self.game_is_on():
            print("Next question is:")

    def check_answer(self, correct_answer: str, user_answer: str):
        """Checks if the answer is correct. Prints if user was right or wrong\n
        inputs:\n
        **correct_answer** -> str\n
        Answer pulled from object from question_list\n
        **user_answer** -> str\n
        answer given by user"""
        print(f"The correct answer is {correct_answer}")
        return correct_answer == user_answer

    def game_is_on(self):
        """Checks if the quiz ran out of questions\n
        compares attribute **question_number** with length of attribute **question_list**"""
        return len(self.question_list) > self.question_number
