import os
import json
from operator import itemgetter

from message import title

config = {
    "messages": {
        "welcome": "Olá, seja bem-vindo ao nosso Quiz sobre Python!",
        "correct": "Boa, resposta correta!",
        "incorrect": "Opa, não foi dessa vez :(",
        "invalid": "\nOpção Inválida!\n",
        "end": "Fim do Quiz",
        "points": "Você fez"
    },
    "points": 0
}

questions_file = open('questions.json', 'r')
questions_data = json.loads(questions_file.read())
questions = questions_data['questions']
questions_file.close()

def print_welcome():
    print(title)
    print(config["messages"]["welcome"])

def print_question(question, index):
    print(f"\n#{question} ({index + 1}/{len(questions)}) Pts: {config['points']}", end="\n")

def print_options(options):
    for index, option in enumerate(options):
        print(f"{index + 1} - {option['text']}")

def print_result(type):
    print("------------------------")
    print(config["messages"][type])
    print("------------------------")

def print_final():
    print(config["messages"]["end"])
    print(f"{config['messages']['points']}: {config['points']}")

def get_answer(options):
    try:
        user_answer_index = int(input("> "))
        user_answer_option = options[user_answer_index - 1]
    except:
        print(config["messages"]["invalid"])
        quit()

    correct_answer = next(i for i in options if i['is_correct'] == True)
    return user_answer_option == correct_answer

def play():
    print_welcome()
    for index, item in enumerate(questions):
        question, options = itemgetter('question', 'options')(item)
        print_question(question, index)
        print_options(options)
        is_correct = get_answer(options)

        if is_correct:
                config["points"] += 1
                print_result("correct")
        else:
            print_result("incorrect")
    print_final()

play()