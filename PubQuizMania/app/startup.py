import yaml


from experiments.terminal_app import CategoryConstants, QuestionConstants
from PubQuizMania.app.models import Category, Question
from PubQuizMania.app.repository import QuizRepository


def start_script():
    import_categories()
    import_data()


def import_questions_from_yaml(filename):
    data = dict()

    with open(filename, "r") as f:
        data = yaml.load(f)

    return [
        Question(
            x[QuestionConstants.NUMBER],
            x[QuestionConstants.QUESTION],
            x[QuestionConstants.ANSWER],
            x[QuestionConstants.CATEGORIES] if QuestionConstants.CATEGORIES in x else [],
        )
        for x in data["questions"]
    ]


def import_data():
    questions = import_questions_from_yaml("./experiments/questions.yml")

    repository = QuizRepository()
    repository.delete_questions()

    for question in questions:
        if not repository.does_question_exist(question.number):
            repository.add_question(question)


def import_categories():
    repository = QuizRepository()
    all_categories = Category.get_all_categories()

    for category in all_categories:
        repository.add_category_if_not_exists(category)
