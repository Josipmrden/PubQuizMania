from PubQuizMania.app.repository import QuizRepository


class QuizService:
    def __init__(self):
        self.repository = QuizRepository()

    def get_random_quiz(self, no_questions, topics=[]):
        if no_questions <= 0:
            return []
        return self.repository.get_quiz(no_questions, topics)

    def get_unlabelled_question(self):
        return self.repository.get_unlabelled_question()
