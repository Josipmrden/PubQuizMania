import django

django.setup()


from PubQuizMania.settings import db
from experiments.terminal_app import CategoryConstants, QuestionConstants
from PubQuizMania.app.models import Category, Question, Quiz, UnlabeledQuestions


class QuizRepository:
    def __init__(self):
        self.db = db
        self.quiz_collection = db.get_collection("quiz_app_question")
        self.category_collection = db.get_collection("category")

    def get_quiz(self, no_questions, topics=[]):
        if not topics:
            results = list(self.quiz_collection.aggregate([{"$sample": {"size": no_questions}}]))
        else:
            results = list(
                self.quiz_collection.aggregate(
                    [
                        {"$match": {"groups": {"$in": topics}}},
                        {"$sample": {"size": no_questions}},
                    ]
                )
            )

        questions = []
        for result in results:
            questions.append(
                Question(
                    result[QuestionConstants.NUMBER],
                    result[QuestionConstants.QUESTION],
                    result[QuestionConstants.ANSWER],
                    [],
                )
            )

        return Quiz(questions)

    def get_unlabeled_question(self, no_questions: int, random: bool):
        if random:
            results = list(
                self.quiz_collection.aggregate(
                    [{"$match": {"groups": {"$exists": False}}}, {"$sample": {"size": no_questions}}]
                )
            )
        else:
            results = list(self.quiz_collection.find({"groups": {"$exists": False}}).limit(no_questions))

        questions = []
        for result in results:
            questions.append(
                Question(
                    result[QuestionConstants.NUMBER],
                    result[QuestionConstants.QUESTION],
                    result[QuestionConstants.ANSWER],
                    [],
                )
            )

        return UnlabeledQuestions(questions)

    def does_question_exist(self, question_number):
        return self.quiz_collection.find({QuestionConstants.NUMBER: question_number}).count() > 0

    def add_question(self, question: Question):
        self.quiz_collection.insert(
            {
                QuestionConstants.NUMBER: question.number,
                QuestionConstants.QUESTION: question.question,
                QuestionConstants.ANSWER: question.answer,
                QuestionConstants.CATEGORIES: question.categories,
            }
        )

    def update_question(self, question: Question):
        if not self.does_question_exist(question.number):
            return LabelingQuestionInsertionStatus(False, "Question does not exist!")

        self.quiz_collection.update_one(
            {QuestionConstants.NUMBER: question.number},
            {
                "$set": {
                    QuestionConstants.QUESTION: question.question,
                    QuestionConstants.ANSWER: question.answer,
                    QuestionConstants.CATEGORIES: question.categories,
                }
            },
        )

    def delete_questions(self):
        self.quiz_collection.remove({})

    def get_categories(self):
        results = self.category_collection.find()
        categories = []

        for result in results:
            categories.append(
                Category(name=result[CategoryConstants.NAME], abbreviation=result[CategoryConstants.ABBREVIATION])
            )

        return categories

    def add_category_if_not_exists(self, category: Category):
        self.category_collection.update_one(
            {CategoryConstants.ABBREVIATION: category.abbreviation},
            {"$set": {CategoryConstants.NAME: category.name, CategoryConstants.ABBREVIATION: category.abbreviation}},
            upsert=True,
        )

    def update_question_categories(self, question_number, categories):
        if not self.does_question_exist(question_number):
            return LabelingQuestionInsertionStatus(False, "Question does not exist!")

        self.quiz_collection.update_one(
            {QuestionConstants.NUMBER: question_number}, {"$set": {QuestionConstants.CATEGORIES: categories}}
        )

        return LabelingQuestionInsertionStatus(True, "")


class LabelingQuestionInsertionStatus:
    def __init__(self, success: bool, info: str):
        self.success = success
        self.info = info
