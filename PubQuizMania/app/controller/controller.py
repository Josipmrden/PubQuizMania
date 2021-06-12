from django.http import JsonResponse

from rest_framework.decorators import api_view

from PubQuizMania.app.controller.validation import parse_question_params
from PubQuizMania.app.serializers import QuizJsonifier, QuestionJsonifier
from PubQuizMania.app.service import QuizService

quiz_service = QuizService()


@api_view(["GET"])
def get_random_quiz(request):
    no_questions, topics = parse_question_params(request)
    quiz = quiz_service.get_random_quiz(no_questions, topics)
    json_quiz = QuizJsonifier().jsonify(quiz)

    return JsonResponse(json_quiz)


@api_view(["GET"])
def get_unlabeled_question(request):
    question = quiz_service.get_unlabelled_question()
    data = QuestionJsonifier().jsonify(question)
    return JsonResponse(data)
