import Text as tf
from datetime import datetime


def input_choice(size: int, message: str):
    while True:
        number = input(message)
        if number.isdigit() and 0 < int(number) < size + 1:
            return int(number)
        else:
            print(tf.wrong_choice(size))


def main_menu() -> int:
    print(*tf.menu, sep='\n')
    return input_choice(len(tf.menu) - 1, tf.input_choice)


def show_note(book: list[dict[str, str]], message: str):
    if book:
        print('\n' + '=' * 195)
        for i, note in enumerate(book, 1):
            print(f'{i:<3} | {note["data"]: <20} | {note["name"]: <20} '
                  f' | {note["body"]: <20}')
        print('=' * 195 + '\n')
    else:
        print(message)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def input_note(message: list[str]) -> dict[str, str]:
    note = {}
    now = datetime.now()
    data = now.strftime("%d/%m/%y %I:%M %p")
    name = input(message[0])
    body = input(message[1])
 
    if data:
        note['data'] = data
    if name:
        note['name'] = name
    if body:
        note['body'] = body
    return note


def input_index(message: str, pb: list, error: str) -> int:
    show_note(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)


def find_data():
    note = input(tf.for_find_data)
    return note
def find_name():
    note = input(tf.for_find_name)
    return note

def close()->str:
    return tf.close