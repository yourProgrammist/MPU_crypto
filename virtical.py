from typing import List
from termcolor import colored
import math
from pprint import pprint
from typing import List


def all_indexes(key: str, ch: str) -> List[int]:
    """
    Search all occurrence in string
    :param key: str
    :param ch: str
    :return: List[int]
    """
    return [index for index, i in enumerate(key) if i == ch]


def arr_from_key(key: str) -> List[int]:
    """
    :param key: str
    :return: List[int]
    """
    arr = [0 for _ in range(len(key))]
    indexes = {}
    for i in key:
        indexes[i] = all_indexes(key, i)
    indexes = dict(sorted(indexes.items(), key=lambda x:x[0]))
    idx = 1
    for i in indexes:
        for index in indexes[i]:
            arr[index] = idx
            idx += 1
    return arr


def encrypt(message: str, key: str) -> str:
    """
    Encrypt message with vertical crypto
    :param message: str
    :param key: str
    :return: str
    """
    message = list(message)
    arr = arr_from_key(key)
    n = len(arr)

    matrix = [['' for _ in range(n)] for _ in range(math.ceil(len(message) / n))]
    cols, rows = len(matrix[0]), len(matrix)
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = message.pop(0)
            if not message:
                break
    tmp = []
    for col in range(cols):
        tmp.append(''.join([matrix[row][col] for row in range(rows)]))
    return ''.join([x[0] for x in sorted(zip(tmp, arr), key=lambda x:x[1])])


def decrypt(encypted_message: str, key: str) -> str:
    """
    Decrypt message with vertical crypto
    :param encypted_message: str
    :param key: str
    :return: str
    """
    encypted_message = list(encypted_message)
    arr = arr_from_key(key)
    print(arr)
    matrix = [['' for _ in range(len(arr))] for _ in range(math.ceil(len(encypted_message) / len(arr)))]
    long = (len(encypted_message) % len(arr))
    idx = 1
    while idx <= len(arr):
        x = arr.index(idx)
        offset = 0
        if x >= long and long != 0:
            offset = 1
        for row in range(len(matrix) - offset):
            matrix[row][x] = encypted_message.pop(0)
        idx += 1
    return ''.join([''.join(x) for x in matrix]).replace('прб', ' ').replace('зпт', ',').replace('тчк', '.')


def vertical():
    choice = int(input("Что вы хотите сделать: зашифровать (1) или расшифровать (2)?"))
    key = input("Введите ключ: ")
    message = input("Введите сообщение: ").replace(" ", "прб").replace(",", "зпт").replace(".", 'тчк').replace(':', '').replace(';', '').replace('!', '').replace('?', '').lower()
    if choice == 1:
        print(colored(f"Зашифрованное сообщение {encrypt(message, key)}", 'red'))
    else:
        print(colored(f"Расшифрованное сообщение {decrypt(message, key)}", 'red'))

if __name__ == '__main__':
    vertical()