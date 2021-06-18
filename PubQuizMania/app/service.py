from typing import List

from PubQuizMania.app.models import AvailableCategories, Question, LabelingStats
from PubQuizMania.app.repository import QuizRepository, LabelingQuestionInsertionStatus


class QuizService:
    def __init__(self):
        self.repository = QuizRepository()

    def get_random_quiz(self, no_questions, topics=[]):
        if no_questions <= 0:
            return []
        return self.repository.get_quiz(no_questions, topics)

    def get_unlabeled_question(self, no_questions: int, random: bool, excluded_questions: List[int]):
        return self.repository.get_unlabeled_question(no_questions, random, excluded_questions)

    def get_categories(self):
        categories = self.repository.get_categories()
        return AvailableCategories(categories)

    def label_question(self, question: Question):
        available_categories = self.get_categories()
        available_abbreviations = [x.abbreviation for x in available_categories.categories]

        for category in question.categories:
            if category not in available_abbreviations:
                return LabelingQuestionInsertionStatus(False, "Invalid labels!")

        return self.repository.update_question(question)

    def get_labeling_stats(self) -> LabelingStats:
        number_of_labeled_questions = self.repository.get_number_of_labeled_questions()
        number_of_total_questions = self.repository.get_number_of_total_questions()

        return LabelingStats(number_of_labeled_questions, number_of_total_questions)
