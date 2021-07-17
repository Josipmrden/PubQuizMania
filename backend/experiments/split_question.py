import re


def separate_questions_and_answers(filename_src):
    f = open(filename_src, "r")

    lines = f.readlines()

    for line in lines:
        question_number_result = re.search("^\d{1,}\.", line)
        question_number_indexes = question_number_result.regs[0]
        question_mark_index = line.index("?")

        _ = int(line[: question_number_indexes[1] - 1])
        _ = line[question_number_indexes[1] + 1 : question_mark_index + 1].strip()
        _ = line[question_mark_index + 1 :].strip()

    f.close()


if __name__ == "__main__":
    separate_questions_and_answers("../questions3.txt")
