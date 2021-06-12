import re

from PubQuizMania.app.models import Question


def start_script():
    pass


def get_questions(filename):
    questions = []

    f = open(filename, "r")

    lines = f.readlines()
    for line in lines:
        question_number_result = re.search("^\d{1,}\.", line)
        question_number_indexes = question_number_result.regs[0]
        question_mark_index = line.index("?")

        question_number = int(line[: question_number_indexes[1] - 1])
        question = line[question_number_indexes[1] : question_mark_index + 1].strip()
        answer = line[question_mark_index + 1 :].strip()

        question_model = Question(
            number=question_number, question=question, answer=answer
        )
        questions.append(question_model)
    f.close()

    return questions


def import_data():
    questions = get_questions("../experiments/questions3.txt")

    for question in questions:
        result = Question.objects.filter(number=question.number)
        if len(result) == 0:
            question.save()
