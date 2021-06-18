from typing import Tuple, List
from urllib.parse import parse_qs


from PubQuizMania.app.controller.request import QuizRequest
from PubQuizMania.app.models import Question

DEFAULT_NO_QUESTIONS = 10
DEFAULT_NO_UNLABELED_QUESTIONS = 1


def parse_question_params(request) -> Tuple[int, List]:
    param_dictionary = parse_qs(request.GET.urlencode())

    no_questions = (
        param_dictionary[QuizRequest.NO_QUESTIONS][0]
        if QuizRequest.NO_QUESTIONS in param_dictionary
        else DEFAULT_NO_QUESTIONS
    )
    try:
        no_questions = int(no_questions)
        if no_questions <= 0:
            no_questions = DEFAULT_NO_QUESTIONS
    except:
        no_questions = DEFAULT_NO_QUESTIONS

    topics = param_dictionary[QuizRequest.TOPICS][0].split(",") if QuizRequest.TOPICS in param_dictionary else []

    return no_questions, topics


def parse_unlabeled_question_request(request) -> int:
    param_dictionary = parse_qs(request.GET.urlencode())

    no_questions = (
        param_dictionary[QuizRequest.NO_QUESTIONS][0]
        if QuizRequest.NO_QUESTIONS in param_dictionary
        else DEFAULT_NO_UNLABELED_QUESTIONS
    )
    try:
        no_questions = int(no_questions)
        if no_questions <= 0:
            no_questions = DEFAULT_NO_UNLABELED_QUESTIONS
    except:
        no_questions = DEFAULT_NO_UNLABELED_QUESTIONS

    random = False
    if QuizRequest.RANDOM in param_dictionary:
        try:
            random = bool(param_dictionary[QuizRequest.RANDOM])
        except:
            pass

    excluded_questions = []

    if QuizRequest.EXCLUDED_QUESTIONS in param_dictionary:
        question_number_strings = param_dictionary[QuizRequest.EXCLUDED_QUESTIONS][0].split(",")
        for number in question_number_strings:
            try:
                excluded_questions.append(int(number))
            except:
                excluded_questions = []
                break

    return no_questions, random, excluded_questions


class LabeledQuestionValidationStatus:
    QUESTION_NUMBER = "question_number"
    QUESTION = "question"
    ANSWER = "answer"
    CATEGORIES = "categories"

    def __init__(self, success: bool, question: Question, info: str) -> None:
        self.success = success
        self.question = question
        self.info = info


def parse_labeled_question(request):
    data = request.data
    question = None
    answer = None
    question_number = 0
    categories = []

    invalid_status = LabeledQuestionValidationStatus(False, question, "Invalid parameters!")

    if LabeledQuestionValidationStatus.QUESTION_NUMBER not in data:
        return invalid_status

    if LabeledQuestionValidationStatus.CATEGORIES not in data:
        return invalid_status

    try:
        question_number = int(data[LabeledQuestionValidationStatus.QUESTION_NUMBER])
        categories = data[LabeledQuestionValidationStatus.CATEGORIES]
    except:
        return invalid_status

    if question_number <= 0 or len(categories) == 0:
        return invalid_status

    if LabeledQuestionValidationStatus.QUESTION not in data:
        return invalid_status

    question = data[LabeledQuestionValidationStatus.QUESTION]

    if LabeledQuestionValidationStatus.ANSWER not in data:
        return invalid_status

    answer = data[LabeledQuestionValidationStatus.ANSWER]

    question_object = Question(question_number, question, answer, categories)

    return LabeledQuestionValidationStatus(True, question_object, "")
