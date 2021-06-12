import django

django.setup()


from PubQuizMania.settings import db
from experiments.terminal_app import QuestionConstants
from PubQuizMania.app.models import Question, Quiz


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

        questions = []
        for result in results:
            questions.append(
                Question(
                    result[QuestionConstants.NUMBER],
                    result[QuestionConstants.QUESTION],
                    result[QuestionConstants.ANSWER],
                )
            )

        return Quiz(questions)

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
