import json
import sys
from pprint import pprint


def count_questions(data: dict) -> None:
    # вывести количество вопросов (questions)
    question_count = 0
    rounds = data['game']['rounds']
    for round in rounds:
        question_count += len(round['questions'])
    print(f'There are {question_count} questions')


def print_right_answers(data: dict) -> None:
    # вывести все правильные ответы (correct_answer)
    right_answers = []
    rounds = data['game']['rounds']
    for round in rounds:
        questions = round['questions']
        for question in questions:
            right_answers.append(question['correct_answer'])
    print('Right answers:', right_answers)


def print_max_answer_time(data: dict) -> None:
    # вывести максимальное время ответа (time_to_answer)
    maxtime = 0
    rounds = data['game']['rounds']
    for round in rounds:
        if round['settings']['time_to_answer'] > maxtime:
            maxtime = round['settings']['time_to_answer']
    print('Max answer times is', maxtime)


def main(args):
    data = json.load(open(args))  # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    main(sys.argv[-1])
