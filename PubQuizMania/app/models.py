from experiments.terminal_app import CategoryConstants
from typing import List

from .serializers import JsonSerializable


class Question(JsonSerializable):
    def __init__(self, number: int, question: str, answer: str, categories: List[str]):
        self.number = number
        self.question = question
        self.answer = answer
        self.categories = categories

    def to_json(self):
        return {"number": self.number, "question": self.question, "answer": self.answer, "categories": self.categories}


class Quiz(JsonSerializable):
    def __init__(self, questions: List[Question]):
        self.questions = questions

    def to_json(self):
        questions_json = [x.to_json() for x in self.questions]
        return {"questions": questions_json}


class UnlabeledQuestions:
    def __init__(self, questions: List[Question]):
        self.questions = questions

    def to_json(self):
        questions_json = [x.to_json() for x in self.questions]
        return {"unlabeled_questions": questions_json}


class Category(JsonSerializable):
    def __init__(self, name: str, abbreviation: str) -> None:
        self.name = name
        self.abbreviation = abbreviation

    def to_json(self):
        return {CategoryConstants.NAME: self.name, CategoryConstants.ABBREVIATION: self.abbreviation}

    @classmethod
    def get_all_categories(cls):
        return [
            Category("POVIJEST", "POV"),
            Category("GEOGRAFIJA", "GEO"),
            Category("GEOGRAFIJA HRVATSKE", "HGEO"),
            Category("POVIJEST HRVATSKE", "HPOV"),
            Category("ANTIČKA POVIJEST", "APOV"),
            Category("UMJETNOST", "UMJ"),
            Category("MEDICINA", "MED"),
            Category("STEM", "STEM"),
            Category("BIOLOGIJA", "BIO"),
            Category("KEMIJA", "KEM"),
            Category("ZNANOST", "ZNS"),
            Category("SPORT", "SPO"),
            Category("SLIKARSTVO", "SLI"),
            Category("2. SVJETSKI RAT", "WWII"),
            Category("1. SVJETSKI RAT", "WWI"),
            Category("RAZNO", "RZN"),
            Category("FLORA I FAUNA", "FF"),
            Category("GASTRONOMIJA", "GSN"),
            Category("FILOZOFIJA", "FIL"),
            Category("NOGOMET", "NOG"),
            Category("KNJIŽEVNOST", "KNJ"),
            Category("GLAZBA", "GLA"),
            Category("JEZIK", "JEZ"),
            Category("FILM", "FLM"),
            Category("STRIP", "STR"),
            Category("HRVATSKI FILM", "HFLM"),
            Category("RELIGIJA", "REL"),
            Category("POLITIKA", "POL"),
            Category("SVEMIR", "SVE"),
        ]


class AvailableCategories(JsonSerializable):
    def __init__(self, categories: List[Category]):
        self.categories = categories

    def to_json(self):
        categories_json = [x.to_json() for x in self.categories]
        return {"categories": categories_json}


class LabeledCategories:
    def __init__(self, data):
        self.categories = data.categories


class LabelingStats:
    def __init__(self, labeled_questions, total_questions) -> None:
        self.labeled_questions = labeled_questions
        self.total_questions = total_questions

    def to_json(self):
        return {"total_questions": self.total_questions, "labeled_questions": self.labeled_questions}
