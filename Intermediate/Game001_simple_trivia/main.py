import sys
sys.path.insert(0, "python/")
from python import data, quiz_brain

quiz = quiz_brain.QuizBrain()

while quiz.game_is_on():
    quiz.next_question()
message = [data.scores[q] for q in data.scores if quiz.score in q]
print(f"Your score is: {quiz.score}/{len(quiz.question_list)}"
      f" ({round((quiz.score / len(quiz.question_list)) * 100, 2)}%).\n{message[0]}")
