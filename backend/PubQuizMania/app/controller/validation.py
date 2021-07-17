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

    topics = (
        param_dictionary[QuizRequest.CATEGORIES][0].split(",") if QuizRequest.CATEGORIES in param_dictionary else []
    )

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


class InvalidLabelingConstants:
    INVALID_PARAMS = "Invalid parameters!"
    NO_CATEGORIES = "Categories not specified!"
    NO_QUESTION = "Question not specified!"
    NO_ANSWER = "Answer not specified!"
    NO_NUMBER = "Question number not specified!"


def parse_labeled_question(request):
    data = request.data
    question = None
    answer = None
    question_number = 0
    categories = []

    if LabeledQuestionValidationStatus.QUESTION_NUMBER not in data:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_NUMBER)

    if LabeledQuestionValidationStatus.CATEGORIES not in data:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_CATEGORIES)

    try:
        question_number = int(data[LabeledQuestionValidationStatus.QUESTION_NUMBER])
        categories = data[LabeledQuestionValidationStatus.CATEGORIES]
    except:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.INVALID_PARAMS)

    if question_number <= 0:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_NUMBER)

    if len(categories) == 0:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_CATEGORIES)

    if LabeledQuestionValidationStatus.QUESTION not in data:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_QUESTION)

    question = data[LabeledQuestionValidationStatus.QUESTION]

    if len(question) == 0:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_QUESTION)

    if LabeledQuestionValidationStatus.ANSWER not in data:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_ANSWER)

    answer = data[LabeledQuestionValidationStatus.ANSWER]

    if len(str(answer)) == 0:
        return LabeledQuestionValidationStatus(False, question, InvalidLabelingConstants.NO_ANSWER)

    question_object = Question(question_number, question, answer, categories)

    return LabeledQuestionValidationStatus(True, question_object, "")


class AnsweredQuestionValidationStatus:
    QUESTION_NUMBER = "questionNumber"
    ANSWER = "answer"

    def __init__(self, question_number: int, answer: str, success: bool) -> None:
        self.question_number = question_number
        self.answer = answer
        self.success = success


def parse_answered_question(request):
    data = request.data
    if (
        AnsweredQuestionValidationStatus.QUESTION_NUMBER not in data
        or AnsweredQuestionValidationStatus.ANSWER not in data
    ):
        return AnsweredQuestionValidationStatus(0, 0, False)

    question_number = data[AnsweredQuestionValidationStatus.QUESTION_NUMBER]
    answer = data[AnsweredQuestionValidationStatus.ANSWER]

    return AnsweredQuestionValidationStatus(question_number, answer, True)
