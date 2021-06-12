from django.http import HttpResponse
from rest_framework.decorators import api_view

from PubQuizMania.app.controller.validation import parse_question_params
from PubQuizMania.app.serializers import QuestionSerializer
from PubQuizMania.app.service import QuizService

quiz_service = QuizService()


@api_view(["GET"])
def get_random_quiz(request):
    no_questions, topics = parse_question_params(request)
    quiz = quiz_service.get_random_quiz(no_questions, topics)
    data = [QuestionSerializer(x).data for x in quiz]

    return HttpResponse(data)


@api_view(["GET"])
def get_unlabeled_question(request):
    question = quiz_service.get_unlabelled_question()
    data = QuestionSerializer(question.number, question.question, question.answer)
    return HttpResponse(data)
