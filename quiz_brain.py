class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_q.text}. True/False? ")
