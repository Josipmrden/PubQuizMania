from typing import List

from PubQuizMania.app.models import AvailableCategories
from PubQuizMania.app.repository import QuizRepository, LabelingQuestionInsertionStatus


class QuizService:
    def __init__(self):
        self.repository = QuizRepository()

    def get_random_quiz(self, no_questions, topics=[]):
        if no_questions <= 0:
            return []
        return self.repository.get_quiz(no_questions, topics)

    def get_unlabeled_question(self, no_questions: int, random: bool = False):
        return self.repository.get_unlabeled_question(no_questions, random)

    def get_categories(self):
        categories = self.repository.get_categories()
        return AvailableCategories(categories)

    def label_question(self, question_number: int, categories: List[str]):
        available_categories = self.get_categories()
        available_abbreviations = [x.abbreviation for x in available_categories.categories]

        for category in categories:
            if category not in available_abbreviations:
                return LabelingQuestionInsertionStatus(False, "Invalid labels!")

        return self.repository.update_categories(question_number, categories)
