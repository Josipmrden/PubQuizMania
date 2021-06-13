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


if __name__ == "__main__":
    filename = "../questions.yml"
    import_data(filename)
