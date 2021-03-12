from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for data in question_data:
    Question_text = data["question"]
    Question_answer = data["correct_answer"]
    new_question = Question(Question_text, Question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text) así se llama a un dato de un objeto en una lista.

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}.")