import yaml

from experiments.terminal_app import QuestionConstants, get_question_collection


def import_data(filename):
    data = dict()
    with open(filename, "r") as f:
        data = yaml.load(f)

    collection = get_question_collection()
    for question in data["questions"]:
        result = collection.find_one({"number": question["number"]})
        if result is None:
            collection.insert_one(question)
        else:
            collection.update_one({"_id": result["_id"]}, {"$set": question})


def export_data():
    collection = get_question_collection()
    questions = collection.find({})

    data = dict()

    question_dicts = list()
    for question in questions:
        question_dict = dict()
        question_dict[QuestionConstants.NUMBER] = question[QuestionConstants.NUMBER]
        question_dict[QuestionConstants.QUESTION] = question[QuestionConstants.QUESTION]
        question_dict[QuestionConstants.ANSWER] = question[QuestionConstants.ANSWER]
        question_dicts.append(question_dict)

    data["questions"] = question_dicts
    with open("../questions.yml", "w") as outfile:
        yaml.dump(data, outfile, allow_unicode=True, sort_keys=False)


if __name__ == "__main__":
    filename = "../questions.yml"
    # export_data('../questions.yml')
    import_data(filename)
