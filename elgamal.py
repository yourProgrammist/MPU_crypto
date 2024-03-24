import random
import math
from typing import List
import getpass

import sympy
from Crypto.Util import number

class BaseErrorCrypt(Exception):
    """Base error class for crypt-error"""
    pass


class KeyError(BaseErrorCrypt):
    """Error for secret key"""
    pass


class MessageError(BaseErrorCrypt):
    """Error for message"""
    pass



class Crypt:
    __slots__ = ("_message", "_ALP")

    __replace_chars = ":?'\"\/[]{}<>-—., "

    def __replace_char(self, char: chr) -> str:
        if char == '.':
            return "тчк"
        if char == ',':
            return "зпт"
        if char == ' ':
            return "прб"
        if char == 'ё':
            return 'е'
        if char in self._ALP:
            return char
        return ""

    @classmethod
    def _replace_to_char(cls, message: str) -> str:
        return message.replace("тчк", '.').replace("зпт", ',').replace("прб", " ")

    def __strip_message(self, message: str) -> str:
        """Validate message"""
        if not message:
            raise MessageError(f'Message is empty')
        if all([ch.isdigit() for ch in message.split()]):
            return message
        reformat_message = ""
        for ch in message.lower():
            if ch in self._ALP or ch in self.__replace_chars:
                reformat_message += self.__replace_char(ch)
        if reformat_message.strip(self.__replace_chars).strip(self._ALP):
            raise MessageError(f'{reformat_message} include forbidden characters')
        return reformat_message

    def __init__(self, message: str):
        self._ALP = 'qабвгдежзийклмнопрстуфхцчшщъыьэюя'
        self._message = self.__strip_message(message)

    def get_message(self) -> str:
        return self._message

    def set_message(self) -> None:
        self._message = self.__strip_message(self._message)

    def __str__(self) -> str:
        return f'Crypt for {self._message}'



COUNT_RANDOMIZER=3

class Elgamal(Crypt):
    __slots__ = ("k", "p", "__x", "g", "y")
    __bits_in_keys = 7

    @staticmethod
    def __validate_on_prime(param: int) -> int:
        for i in range(2, int(param ** 0.5)):
            if param % i == 0:
                raise KeyError(f"{param} is not a prime number")
        return param

    def __generate_random(self) -> List[int]:
        self.k = []
        while len(self.k) < COUNT_RANDOMIZER:
            tmp = random.choice(range(1, self.p - 1))
            if math.gcd(tmp, self.p - 1) == 1 and tmp not in self.k:
                self.k.append(tmp)

        return self.k

    def __init__(self, message: str):
        super().__init__(message)
        self.p = number.getPrime(self.__bits_in_keys)
        self.__x = random.choice(range(2, self.p))
        self.g = random.choice(range(2, self.p))
        self.y = (self.g ** self.__x) % self.p
        self.k = self.__generate_random()


    def __str__(self):
        return f'OPENED KEYS:\np = {self.p}\ng = {self.g}\ny = {self.y}\nk = {self.k}\nCLOSED KEYS:\nx = {self.__x}'

    def set_keys(self, p: int, x: int, g: int) -> None:
        self.p = self.__validate_on_prime(p)
        assert p > len(self._ALP)
        self.__x = x
        self.g = g
        assert 1 < x < p and 1 < g < p
        self.y = (self.g ** self.__x) % self.p
        print(f"OPENED KEY Y={self.y}\tG={self.g}\tP={self.p}\nCLOSED KEY X={self.__x}")
        self.k = self.__generate_random()
        print(f"RANDOMIZATORS {self.k}")

    def get_keys(self) -> tuple:
        return self.p, self.__x, self.g, self.y, self.k

    def encrypt(self):
        m = [self._ALP.index(i) for i in self._message]
        tmp = []
        for ch in m:
            r = random.choice(self.k)
            ai = (self.g ** r) % self.p
            bi = (self.y ** r * ch) % self.p
            tmp += [ai, bi]
        res = list(map(str, tmp))
        for i in range(len(res)):
            tmp = res[i]
            res[i] = tmp.rjust(len(str(self.p)), '0')
        result = ''.join(res)
        res = list(''.join(res))
        q = []
        while res:
            if len(q) == 5:
                print(''.join(q))
                q = []
            else:
                q.append(res.pop(0))
        return result

    def find_x(self, a, b, m) -> int:
        if math.gcd(a, m) == 1:
            a_inverse = pow(a, -1, m)
            x = (a_inverse * b) % m
            return x
        return 0

    def decrypt(self, key_p: int, key_x: int):
        return self._replace_to_char(''.join([self._ALP[self.find_x(int(''.join([self._message[i + j] for j in range(len(str(key_p)))])) ** key_x, int(''.join([self._message[i + j] for j in range(len(str(key_p)), 2 * len(str(key_p)))])), key_p)] for i in range(0, len(message), 2 * len(str(key_p)))]))

def elgamal():
    message = input("Введите сообщение: ")
    choice = int(input("Шифрование - 1, расшифрование - 2"))
    if choice == 1:

        elgamal = Elgamal(message)
        if input("Нужно ли автоматически сгенерировать ключи? y/n").lower() == 'y':

            p, x, g, y, k = elgamal.get_keys()
            print(f"Сгенерированные ключи\np = {p}\nx = {x}\ng = {g}\ny = {y}\nk = {k}")
        else:
            p = int(input("Введите p: "))
            x = int(input("Введите x: "))
            g = int(input("Введите g: "))
            elgamal.set_keys(p, x, g)
        en = elgamal.encrypt()
        print(en)
    elif choice == 2:
        elgamal = Elgamal(message)
        x = int(getpass.getpass("Введите секретный ключ x: "))
        p = int(input("Введите открытый ключ p: "))
        g = int(input("Введите открытый ключ g: "))
        print(elgamal.decrypt(p, x))


if __name__ == "__main__":
    elgamal()