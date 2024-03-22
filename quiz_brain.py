class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def check_answer(self, guess, correct_answer):
        if guess.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_no}.\n")

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        guess = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(guess, current_question.answer)

    def still_has_questions(self):
        return self.question_no < len(self.question_list)

