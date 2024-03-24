import numpy as np
import json
import sys, getopt
RUSSIAN_ALP="абвгдежзийклмнопрстуфхцчшщъыьэюя"

def standart_message(message: str) -> str:
    ans = ""
    for i in range(len(message)):
        if i % 5 == 0 and i != 0:
            ans += " " + message[i]
        else:
            ans += message[i]
    return ans

def inverse_matrix(matrix: list[list]) -> list[list]:
    return np.linalg.inv(np.array(matrix))

def mult_matrix(first_matrix: list[list], second_matrix: list[list]) -> list[list]:
    result = [[0] * len(second_matrix[0]) for _ in range(len(first_matrix))]
    for i in range(len(first_matrix)):
        for j in range(len(second_matrix[0])):
            for k in range(len(second_matrix)):
                result[i][j] += first_matrix[i][k] * second_matrix[k][j]
    return result


def encode(message: str, matrix1: list[list]) -> str:
    result = []
    arr = []
    res = ""
    for i in range(len(message)):
        if 0 <= i < len(message) and message[i] in RUSSIAN_ALP:
            arr.append(RUSSIAN_ALP.index(message[i]) + 1)
    while arr:
        tmp = []
        for i in range(len(matrix1)):
            tmp.append([arr.pop(0)])
        result += mult_matrix(matrix1, tmp)
    for i in result:
        res += str(*i) + ", "
    return res.rstrip(', ')


def decode(encode_message: str, matrix1: list[list]) -> str:
    inv = inverse_matrix(matrix1)
    result = []
    message = []
    tmp = []
    for index in range(len(encode_message)):
        tmp.append(encode_message[index])
        if len(tmp) == 3:
            message.append(int(''.join(tmp)))
            tmp = []

    while message:
        tmp = []
        for i in range(len(matrix1)):
            tmp.append([message.pop(0)])
        result += [round(x[0]) for x in (mult_matrix(inv, tmp))]
    string = ""
    for i in result:
        if 0 <= i - 1 < len(RUSSIAN_ALP):
            string += RUSSIAN_ALP[i - 1]
    return string


def standart_output(message: str) -> str:
    message = [str(int(x)) for x in message.split(',')]
    mx = len(max(message, key=len))
    res = ""
    arr = []
    for i in message:
        while len(i) != mx:
            i = "0" + i
        arr.append(i)
    arr = ''.join(arr)
    return arr

def is_valid(matrix: list[list[int]]) -> bool:
    if len(matrix) == len(matrix[0]) and np.linalg.det(matrix) != 0:
        return True
    return False


def complete_message(message: str, matrix: list[list[int]]) -> str:
    while len(message) % len(matrix) != 0:
        message += 'ф'
    return message

def matrix():
    matrix1 = []
    for i in range(int(input("Введите размероность матрицы и матрицу в виде:\nxxx...x\nxxx...x\nxxx...x\nn="))):
        matrix1.append(list(map(int, input().split())))
    if not is_valid(matrix1):
        print("Invalid matrix")
        exit(1)
    message = input("Введите сообщение - ")
    choice = int(input("Введите режим: 1 - шифрование, 2 - расшифрование - "))

    if choice == 1:
        message = message.replace(' ', 'прб').replace('.', 'тчк').replace(',', 'зпт').replace(';', '').replace(':', '').replace('?', '').replace('!', '').lower()
        message = complete_message(message, matrix1)
        encode_message = encode(message, matrix1)
        print(encode_message)
        print("Шифр")
        print(standart_message(standart_output(encode_message)), '\n')
    elif choice == 2:
        print(decode(message.replace(' ', ''), matrix1).replace('тчк', '.').replace('зпт', ',').replace('прб', ' '))

if __name__ == "__main__":
    matrix()
