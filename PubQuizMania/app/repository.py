import django

django.setup()


from PubQuizMania.settings import db
from experiments.terminal_app import QuestionConstants
from PubQuizMania.app.models import Question


class QuizRepository:
    def __init__(self):
        self.db = db
        self.quiz_collection = db.get_collection("quiz_app_question")

    def get_quiz(self, no_questions, topics=[]):
        if not topics:
            results = list(
                self.quiz_collection.aggregate([{"$sample": {"size": no_questions}}])
            )
        else:
            results = list(
                self.quiz_collection.aggregate(
                    [
                        {"$match": {"groups": {"$in": topics}}},
                        {"$sample": {"size": no_questions}},
                    ]
                )
            )

        quiz = []
        for result in results:
            quiz.append(
                Question(
                    number=result[QuestionConstants.NUMBER],
                    question=result[QuestionConstants.QUESTION],
                    answer=result[QuestionConstants.ANSWER],
                )
            )

        return quiz

    def get_unlabelled_question(self):
        results = list(
            self.quiz_collection.aggregate(
                [{"$match": {"groups": {"$exists": False}}}, {"$sample": {"size": 1}}]
            )
        )

        if not results:
            return None
        result = results[0]

        return Question(
            number=result[QuestionConstants.NUMBER],
            question=result[QuestionConstants.QUESTION],
            answer=result[QuestionConstants.ANSWER],
        )
