from typing import List


class Question:
    def __init__(self, number: int, question: str, answer: str):
        self.number = number
        self.question = question
        self.answer = answer


class Quiz:
    def __init__(self, questions: List[Question]):
        self.questions = questions
