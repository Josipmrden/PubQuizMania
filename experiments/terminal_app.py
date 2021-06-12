from fuzzywuzzy import fuzz
from random import randint
from PubQuizMania.settings import db


class QuestionConstants:
    NUMBER = "number"
    QUESTION = "question"
    ANSWER = "answer"


class Question:
    def __init__(self, number, question, answer):
        self.number = number
        self.question = question
        self.answer = answer


def get_question_collection():
    return db.get_collection("quiz_app_question")


def get_random_question():
    collection = get_question_collection()
    max_question = collection.find_one(sort=[(QuestionConstants.NUMBER, -1)])[
        QuestionConstants.NUMBER
    ]
    random_number = randint(1, max_question)

    question = collection.find_one({QuestionConstants.NUMBER: random_number})

    return Question(
        question[QuestionConstants.NUMBER],
        question[QuestionConstants.QUESTION],
        question[QuestionConstants.ANSWER],
    )


if __name__ == "__main__":

    correct = 0
    total = 0

    while True:
        total += 1
        question = get_random_question()
        written_answer = input(f"{question.number}.{question.question}")
        similarity = fuzz.ratio(written_answer.lower(), question.answer.lower())
        if similarity > 50:
            print(f"Priznato, odgovor je {question.answer}")
            correct += 1
        else:
            print(f"Netočno, odgovor je {question.answer}")

        print(f"Similarity: {similarity}")
        print(f"So far: {correct}/{total}, {correct/total}%")
