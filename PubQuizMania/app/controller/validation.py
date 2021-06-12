from urllib.parse import parse_qs

from PubQuizMania.app.controller.request import RandomQuizRequest


DEFAULT_NO_QUESTIONS = 10


def parse_question_params(request):
    param_dictionary = parse_qs(request.GET.urlencode())

    no_questions = (
        param_dictionary[RandomQuizRequest.NO_QUESTIONS][0]
        if RandomQuizRequest.NO_QUESTIONS in param_dictionary
        else DEFAULT_NO_QUESTIONS
    )
    try:
        no_questions = int(no_questions)
        if no_questions <= 0:
            no_questions = DEFAULT_NO_QUESTIONS
    except:
        no_questions = DEFAULT_NO_QUESTIONS

    topics = (
        param_dictionary[RandomQuizRequest.TOPICS][0].split(",")
        if RandomQuizRequest.TOPICS in param_dictionary
        else []
    )

    return no_questions, topics
