from ques_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question_set in question_data:
        text_1 = question_set["question"]
        answer_1 = question_set["correct_answer"]
        new_question = Question(text_1,answer_1)
        question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.questions_number}")
