from copy import deepcopy
import random
trafar = [
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 0]
]
RUSSIAN_ALP="абвгдежзийклмнопрстуфхцчшщъыьэюя"

def rotate_1(trafar):
    new_matrix = []
    for row in range(len(trafar)):
        new_matrix.append(trafar[row][::-1])
    return new_matrix

def rotate_2(trafar):
    new_matrix = []
    for row in range(len(trafar)):
        new_matrix.append(trafar[5-row])
    return new_matrix


def step(tmp_matrix, message):
    for i in range(len(trafar)):
        for j in range(len(trafar[0])):
            if not tmp_matrix[i][j] and not trafar[i][j]:
                tmp_matrix[i][j] = message.pop(0)
def encrypt(message, trafar):

    while len(message) % 60 != 0:
        message += RUSSIAN_ALP[random.choice(range(0, 32))]
    res=''
    while message:
        tmp_trafar = deepcopy(trafar)
        tmp_matrix = [['' for _ in range(10)] for _ in range(6)]
        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not tmp_matrix[i][j] and not trafar[i][j]:
                    tmp_matrix[i][j] = message.pop(0)




        trafar = rotate_1(trafar)
        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not tmp_matrix[i][j] and not trafar[i][j]:
                    tmp_matrix[i][j] = message.pop(0)
        trafar = rotate_2(trafar)


        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not tmp_matrix[i][j] and not trafar[i][j]:
                    tmp_matrix[i][j] = message.pop(0)

        trafar = rotate_1(trafar)


        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not tmp_matrix[i][j] and not trafar[i][j]:
                    tmp_matrix[i][j] = message.pop(0)
        for row in tmp_matrix:
            res += ''.join(row)
        trafar = tmp_trafar
    return res

def decrypt(message, trafar):
    res = ''
    l = len(message)

    while len(res) < l:
        tmp_matrix = [['' for _ in range(10)] for _ in range(6)]
        for i in range(len(tmp_matrix)):
            for j in range(len(tmp_matrix[0])):
                tmp_matrix[i][j] = message.pop(0)
        tmp_trafar = deepcopy(trafar)
        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not trafar[i][j]:
                    res += tmp_matrix[i][j]
        trafar = rotate_1(trafar)
        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not trafar[i][j]:
                    res += tmp_matrix[i][j]
        trafar = rotate_2(trafar)
        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not trafar[i][j]:
                    res += tmp_matrix[i][j]
        trafar = rotate_1(trafar)
        for i in range(len(trafar)):
            for j in range(len(trafar[0])):
                if not trafar[i][j]:
                    res += tmp_matrix[i][j]
        trafar = tmp_trafar
    return res

def cardano():
    choice = int(input("Введите 1 для шифрования, 2 для расшифрование"))
    message = list(input('Введите сообщение - ').replace(' ', 'прб').lower().replace(',', 'зпт').replace('.', 'тчк'))
    if choice == 1:
        res = encrypt(message, trafar)
        print(f"Зашифрованное сообщение - {res}")
    else:

        print(f"Расшифрованное сообщенеи - {decrypt(list(message), trafar).replace('прб', ' ').replace('зпт', ',').replace('тчк', '.')}")


if __name__ == "__main__":
    cardano()
