from os import error
from typing import Tuple, List
from urllib.parse import parse_qs


from PubQuizMania.app.controller.request import QuizRequest


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

    return no_questions, random


def parse_labeled_question(request):
    data = request.data
    question_number = 0
    categories = []
    error_message = "Invalid parameters"

    if LabeledQuestionValidationStatus.QUESTION_NUMBER not in data:
        return LabeledQuestionValidationStatus(False, question_number, categories, error_message)

    if LabeledQuestionValidationStatus.CATEGORIES not in data:
        return LabeledQuestionValidationStatus(False, question_number, categories, error_message)

    try:
        question_number = int(data[LabeledQuestionValidationStatus.QUESTION_NUMBER])
        categories = data[LabeledQuestionValidationStatus.CATEGORIES]
    except:
        return LabeledQuestionValidationStatus(False, question_number, categories, error_message)

    if question_number <= 0 or len(categories) == 0:
        return LabeledQuestionValidationStatus(False, question_number, categories, error_message)

    return LabeledQuestionValidationStatus(True, question_number, categories, "")


class LabeledQuestionValidationStatus:
    QUESTION_NUMBER = "question_number"
    CATEGORIES = "categories"

    def __init__(self, success: bool, question_number: int, categories: List[str], info: str) -> None:
        self.success = success
        self.question_number = question_number
        self.categories = categories
        self.info = info
