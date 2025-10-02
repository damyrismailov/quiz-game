class QuizBrain:
    def __init__(self, g_list):
        self.questions_number = 0
        self.question_list = g_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.questions_number]
        self.questions_number += 1
        user_input = input(f"Q.{self.questions_number}:{current_question.text} (True/False)")
        self.check_answer(user_input,current_question.answer)

    def still_has_question(self):
      return self.questions_number < len(self.question_list)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.questions_number}")
        print("\n")
