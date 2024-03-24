import math

RUSSIAN_ALP = "qабвгдежзийклмнопрстуфхцчшщъыьэюя"
m = 32

def my_random(a, c):
    global T0
    assert a > 0 and c > 0
    assert a % 2 == 1
    assert math.gcd(c, m) == 1
    assert c < m and a < m
    assert a % 4 == 1
    T0 = (a * T0 + c) % m
    return T0


def encrypt(message: str, a: int, c: int) -> str:
    result = ""
    for index, i in enumerate(message):
        if index == 0:
            result += str(T0 ^ RUSSIAN_ALP.index(i)).zfill(2)
        else:
            result += str(my_random(a, c) ^ RUSSIAN_ALP.index(i)).zfill(2)
    return result


def decrypt(message: str, a: int, c: int) -> str:
    result = ""
    for index in range(0, len(message), 2):
        q = int(message[index]) * 10 + int(message[index + 1])
        if index == 0:
            result += RUSSIAN_ALP[T0 ^ q]
        else:
            result += RUSSIAN_ALP[my_random(a, c) ^ q]
    return result

def shenon():
    choice = int(input("Введите режим: шифрование (1), расшифрование (2)"))
    message = input("Введите сообщение: ").replace('.', 'тчк').replace(',', 'зпт').replace('ё', 'е').replace(':', '').replace(';', '').replace('!', '').replace('-', '').replace(' ', 'прб').lower()
    a = int(input("Введите параметр a: "))
    c = int(input("Введите параметр c: "))
    T0 = int(input("Введите порождающее число T0: "))
    if choice == 1:
        print(f'Зашифрованное сообщение - {encrypt(message, a, c)}')
    else:
        print(f'Расшифрованное сообщение - {decrypt(message, a, c).replace("тчк", ".").replace("зпт", ",").replace("прб", " ")}')


if __name__ == "__main__":
    shenon()




