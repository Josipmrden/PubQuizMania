from PubQuizMania.settings import db


def delete_questions():
    db.get_collection("quiz_app_question").delete_many({})
