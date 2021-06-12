from abc import ABC, abstractmethod
from .models import Question, Quiz
from typing import Any


class Jsonifier(ABC):
    @abstractmethod
    def jsonify(self, object: Any):
        pass


class QuestionJsonifier(Jsonifier):
    def jsonify(self, object: Question):
        return {
            "number": object.number,
            "question": object.question,
            "answer": object.answer,
        }


class QuizJsonifier(Jsonifier):
    def jsonify(self, object: Quiz):
        question_list = []
        question_jsonifier = QuestionJsonifier()
        for q in object.questions:
            question_list.append(question_jsonifier.jsonify(q))

        return {"questions": question_list}
