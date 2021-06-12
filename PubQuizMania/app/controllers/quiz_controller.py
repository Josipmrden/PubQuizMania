from django.http import HttpResponse
from rest_framework.decorators import api_view

from PubQuizMania.app.serializers import QuestionSerializer
from PubQuizMania.app.services import QuizService

quiz_service = QuizService()


@api_view(["GET"])
def get_quiz(request):
    quiz = quiz_service.get_quiz(10, [])
    data = [QuestionSerializer(x).data for x in quiz]

    return HttpResponse(data)


@api_view(["GET"])
def get_quiz_nqt(request, no_questions, topics):
    quiz = quiz_service.get_quiz(no_questions, topics.split(","))
    data = [QuestionSerializer(x).data for x in quiz]

    return HttpResponse(data)


@api_view(["GET"])
def get_unlabeled_question(request):
    question = quiz_service.get_unlabelled_question()
    data = QuestionSerializer(question.number, question.question, question.answer)
    return HttpResponse(data)
