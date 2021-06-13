import pymongo
import yaml

from experiments.terminal_app import QuestionConstants

client = pymongo.MongoClient(
    host="localhost",
    port=27017,
)
db = client.get_database("quiz-db")
quiz_collection = db.get_collection("quiz_app_question")


def export_from_mongo(filename: str):
    results = quiz_collection.find({})

    questions = quiz_collection.find({})

    data = dict()

    question_dicts = list()
    for question in questions:
        question_dict = dict()
        question_dict[QuestionConstants.NUMBER] = question[QuestionConstants.NUMBER]
        question_dict[QuestionConstants.QUESTION] = question[QuestionConstants.QUESTION]
        question_dict[QuestionConstants.ANSWER] = question[QuestionConstants.ANSWER]
        question_dict[QuestionConstants.CATEGORIES] = question[QuestionConstants.CATEGORIES]
        question_dicts.append(question_dict)

    data["questions"] = question_dicts
    with open(filename, "w") as outfile:
        yaml.dump(data, outfile, allow_unicode=True, sort_keys=False)


def main():
    export_from_mongo("./mongo_questions.yml")


if __name__ == "__main__":
    main()
