from data import question_data, new_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in new_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("you have completed this game!")
print(f"your final score was: {quiz.score}/{quiz.question_number}")