REPLACE_LETTER='ф'
SECOND_REPLACE_LETTER='щ'
RUSSIAN_ALP="абвгдежзийклмнопрстуфхцчшщъыьэюя"
message="Выпущенное слово и камень не имеют возврата.".replace(' ', '').replace('.', 'тчк').lower()
def standart_message(message: str) -> str:
    ans = ""
    for i in range(len(message)):
        if i % 5 == 0 and i != 0:
            ans += " " + message[i]
        else:
            ans += message[i]
    return ans

def form_matrix(key: str) -> list[list]:
    key = list(key)
    alp = "абвгдежзиклмнопрстуфхцчшщьыэюя"
    is_visited = set()
    matrix = [[] * 6 for _ in range(5)]
    index = 0
    while key:
        curr_ch = key.pop(0)
        if len(matrix[index]) >= 6:
            index += 1
        matrix[index].append(curr_ch)
        is_visited.add(curr_ch)
    for ch in alp:
        if ch not in is_visited:
            if len(matrix[index]) >= 6:
                index += 1
            matrix[index].append(ch)
            is_visited.add(ch)
    return matrix


def form_bigrams(message: str) -> list[list]:
    message = list(message)
    bigrams = []
    while message:
        if len(message) >= 2:
            if message[0] == message[1]:
                first = message.pop(0)
                second = REPLACE_LETTER
                if first == second:
                    second = SECOND_REPLACE_LETTER
            else:
                first = message.pop(0)
                second = message.pop(0)
        else:
            first = message.pop(0)
            second = REPLACE_LETTER
            if first == second:
                second = SECOND_REPLACE_LETTER # in situation if ["Ф"] and we add second 'Ф'
        bigrams.append([first, second])
    return bigrams

def encode(matrix: list[list], bigrams: list[list], param=1) -> list[list]:
    ans = []
    for i, j in bigrams:
        x1, y1, x2, y2 = get_coords(i, j, matrix)
        if x1 != x2 and y1 != y2:
            ans.append([matrix[x1][y2], matrix[x2][y1]])
        elif x1 == x2:
            if param == 1:
                ans.append([matrix[x1][(y1 + 1) % 6], matrix[x2][(y2 + 1) % 6]])
            else:
                ans.append([matrix[x1][(y1 - 1) % 6], matrix[x2][(y2 - 1) % 6]])
        elif y1 == y2:
            if param == 1:
                ans.append([matrix[(x1 + 1) % 5][y1], matrix[(x2 + 1) % 5][y2]])
            else:
                ans.append([matrix[(x1 - 1) % 5][y1], matrix[(x2 - 1) % 5][y2]])
    return ans




def get_coords(first: str, second: str, matrix: list[list]) -> list[int]:
    x1 = y1 = x2 = y2 = 0
    for ind in range(len(matrix)):
        if first in matrix[ind]:
            x1 = ind
            y1 = matrix[ind].index(first)
        if second in matrix[ind]:
            x2 = ind
            y2 = matrix[ind].index(second)
    return [x1, y1, x2, y2]

def playfair():
    key = input("Введите ключ: - ")
    if len(key) != len(set(key)):
        print("В ключе есть повторы")
        exit(0)

    matrix = form_matrix(key)
    message = input("Введите сообщение - ").replace('.', 'тчк').replace(',', 'зпт').replace(' ', 'прб').lower()
    for i in matrix:
        print(i)
    bigrams = form_bigrams(message)
    encode_message = encode(matrix, bigrams)
    print("ENCODE:    ", standart_message(''.join([''.join(i) for i in encode_message])))
    encode_message = input("Зашифрованное сообщение:").replace(" ", '')
    if len(encode_message) % 2 != 0:
        print("Должно быть четное кол-во элементов")
        #exit(1)
    res = []
    for i in range(0, len(encode_message), 2):
        res.append([encode_message[i], encode_message[i + 1]])
    decode_message = encode(matrix, res, param=2)
    print("DECODE:    ", ''.join([''.join(i) for i in decode_message]).replace('прб', ' ').replace('тчк', '.').replace('зпт', ','))

if __name__ == "__main__":
    playfair()

