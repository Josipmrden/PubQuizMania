import re

question_regex = "^[0-9]+\."


def put_questions_in_one_line(filename_src, filename_dist):
    f = open(filename_src, "r")

    lines = f.readlines()
    new_lines = []
    for line_number in range(1, len(lines) + 1):
        line = lines[line_number - 1].strip()
        regex_search_results = re.search(question_regex, line)
        if regex_search_results is not None:
            new_lines.append(f"{line}\n")
        else:
            last_line = new_lines[-1]
            last_line += f" {line}"
            last_line = last_line.replace("\n", "") + "\n"
            new_lines[-1] = last_line

    f.close()
    f2 = open(filename_dist, "w")
    f2.writelines(new_lines)
    f2.close()


def log_number_not_present_in_question(filename_src):
    f = open(filename_src, "r")
    lines = f.readlines()

    for line_number in range(1, len(lines) + 1):
        line = lines[line_number - 1]
        regex_search_results = re.search(question_regex, line)
        if regex_search_results is None:
            print(f"Line {line_number} not having an order number!")

    f.close()


def allign_number_order(filename_src, filename_dist):
    f = open(filename_src, "r")

    lines = f.readlines()
    new_lines = []

    current_number = 1
    for line_number in range(1, len(lines) + 1):
        line = lines[line_number - 1]
        regex_search_results = re.search(question_regex, line)
        indexes = regex_search_results.regs[0]
        line = str(current_number) + line[indexes[1] - 1 :]

        new_lines.append(line)
        current_number += 1

    f.close()

    f2 = open(filename_dist, "w")
    f2.writelines(new_lines)
    f2.close()


def log_invalid_number_order(filename_src):
    f = open(filename_src, "r")
    lines = f.readlines()

    current_number = 0
    for line_number in range(1, len(lines) + 1):
        line = lines[line_number - 1]
        regex_search_results = re.search(question_regex, line)
        indexes = regex_search_results.regs[0]
        number = int(line[: indexes[1] - 1])
        if number != current_number + 1:
            print(f"Number was {current_number}, next one is {number}")

        current_number = number

    f.close()


def check_question_marks(filename_src):
    f = open(filename_src, "r")
    lines = f.readlines()

    for line_number in range(1, len(lines) + 1):
        line = lines[line_number - 1]
        number_of_question_marks = line.count("?")
        if number_of_question_marks != 1:
            print(
                f"Question {line_number} has {number_of_question_marks} question marks"
            )

    f.close()


if __name__ == "__main__":
    src = "../questions.txt"
    dest = "../questions2.txt"
    final_dest = "../questions3.txt"

    put_questions_in_one_line(src, dest)
    allign_number_order(dest, final_dest)

    log_number_not_present_in_question(dest)
    log_invalid_number_order(final_dest)
    check_question_marks(final_dest)
