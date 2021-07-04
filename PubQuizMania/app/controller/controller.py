from django.http import JsonResponse
from django.http.response import HttpResponse, HttpResponseBadRequest

from rest_framework.decorators import api_view

from PubQuizMania.app.controller.validation import (
    parse_question_params,
    parse_unlabeled_question_request,
    parse_labeled_question,
    parse_answered_question,
)
from PubQuizMania.app.service import QuizService

quiz_service = QuizService()


@api_view(["GET"])
def get_random_quiz(request):
    no_questions, topics = parse_question_params(request)
    quiz = quiz_service.get_random_quiz(no_questions, topics)

    return JsonResponse(quiz.to_json())


@api_view(["GET"])
def get_unlabeled_question(request):

    no_questions, random, excluded_questions = parse_unlabeled_question_request(request)
    unlabeled_questions = quiz_service.get_unlabeled_question(no_questions, random, excluded_questions)
    return JsonResponse(unlabeled_questions.to_json())


@api_view(["GET"])
def get_categories(request):
    available_categories = quiz_service.get_categories()
    return JsonResponse(available_categories.to_json())


@api_view(["POST"])
def label_question(request):
    validation_object = parse_labeled_question(request)

    if not validation_object.success:
        return HttpResponseBadRequest(validation_object.info)

    response = quiz_service.label_question(validation_object.question)

    if not response.success:
        return HttpResponseBadRequest(response.info)

    return HttpResponse()

@api_view(["GET"])
def get_labeling_stats(request):
    stats = quiz_service.get_labeling_stats()

    return JsonResponse(stats.to_json())

@api_view(["POST"])
def answer_question(request):
    validation_object = parse_answered_question(request)

    if not validation_object.success:
        return HttpResponseBadRequest(validation_object.info)

    answer_result = quiz_service.answer_question(validation_object.question_number, validation_object.answer)
    
    return JsonResponse(answer_result.to_json())