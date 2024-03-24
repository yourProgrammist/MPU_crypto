import sys
import readline
readline.set_history_length(10000)
RUSSIAN_ALP = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
SIZE_ALP = len(RUSSIAN_ALP)
SIZE_BUFFER = 20000

ERROR_ALP = 0
ERROR_CHOICE = 1
ERROR_KEY = 2
OK = 0
FAILURE = 1


def index_letter(ch):
    code = -1
    for i, letter in enumerate(RUSSIAN_ALP):
        if ch == letter:
            code = i
            break
    return code


def encode(input_str, key, choice):
    output_str = ""
    for ch in input_str:
        k = index_letter(ch)
        if k != -1:
            if choice == '1':
                output_str += RUSSIAN_ALP[(k + key) % SIZE_ALP]
            elif choice == '2':
                output_str += RUSSIAN_ALP[(k + SIZE_ALP - key) % SIZE_ALP]
        else:
            sys.exit(ERROR_ALP)
    return output_str


def to_standart_message(input_str):
    output_str = ""
    for ch in input_str:
        if ch == ',':
            output_str += "зпт"
        elif ch == '.':
            output_str += "тчк"
        elif ch == 'ё':
            output_str += "е"
        elif ch == ' ':
            output_str += "прб"
        elif ch.lower() in RUSSIAN_ALP:
            output_str += ch.lower()
    return output_str


def from_standart_message(input_str):
    output_str = ""
    i = 0
    while i < len(input_str):
        if i + 2 < len(input_str) and input_str[i:i + 3] == "зпт":
            output_str += ","
            i += 3
        elif i + 2 < len(input_str) and input_str[i:i + 3] == "тчк":
            output_str += "."
            i += 3
        elif i + 2 < len(input_str) and input_str[i:i + 3] == "прб":
            output_str += " "
            i += 3
        else:
            output_str += input_str[i]
            i += 1
    return output_str


def is_valid(key):
    return OK if 0 < key < SIZE_ALP - 1 else FAILURE


def ceaser():
    print("Введите 1 для шифрования, 2 для расшифрования")
    choice = input().strip()
    if choice not in ['1', '2']:
        sys.exit(ERROR_CHOICE)

    print("Введите ключ - ", end="")
    key = int(input().strip())
    if is_valid(key):
        print("Sorry, key must be in range [1, 31]")
        sys.exit(ERROR_KEY)

    print("Введите сообщение - ", end="")
    input_str = input().strip()

    if choice == '1':
        output_str = to_standart_message(input_str)
        output_str = encode(output_str, key, choice)
        print("Зашифрованное сообщение -", output_str)
    elif choice == '2':
        output_str = encode(input_str, key, choice)
        output_str = from_standart_message(output_str)
        print("Расшифрованное сообщение -", output_str)


if __name__ == "__main__":
    ceaser()
