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



"""
TODO:
на вход только E и P, Q - простые и N = P x Q - больше мощности алфавита
Сделать подсказки, какое Q минимальное ввести надо из N / P 
вывести дебаг
"""

class RSA(Crypt):
    __slots__ = ("p", "q", "__n", "__fi", "__e", "__d")
    __bits_in_keys = 8

    @staticmethod
    def __validate_on_prime(param: int) -> int:
        for i in range(2, int(param ** 0.5)):
            if param % i == 0:
                raise KeyError(f"{param} is not a prime number")
        return param

    def __validate_key(self, key):
        if not isinstance(key, int):
            raise KeyError(f"{key} should be an integer")
        return self.__validate_on_prime(key)

    @staticmethod
    def __euclid(a: int, b: int) -> int:
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return max(a, b)

    @staticmethod
    def find_x(a, b, m) -> int:
        if math.gcd(a, m) == 1:
            a_inverse = pow(a, -1, m)
            x = (a_inverse * b) % m
            return x
        else:
            raise KeyError

    def __generate_e(self) -> int:
        tmp = sympy.randprime(2, self.__fi)
        while self.__euclid(tmp, self.__fi) != 1:
            tmp = random.choice(range(2, self.__fi))
        return tmp


    @classmethod
    def __find_fi_from_n(cls, n: int) -> set:
        divs = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divs.add(i)
                divs.add(n // i)
        assert len(divs) == 2
        return divs

    @classmethod
    def __validate_e(cls, e: int, n: int) -> int:
        divs = cls.__find_fi_from_n(n)
        if cls.__euclid(e, (divs.pop() - 1) * (divs.pop() - 1)) != 1:
            raise KeyError
        return e

    @classmethod
    def __validate_d(cls, d: int, e: int, n: int) -> int:
        divs = cls.__find_fi_from_n(n)
        if cls.find_x(e, 1, (divs.pop() - 1) * (divs.pop() - 1)) != d:
            assert KeyError
        return d


    def __init__(self, message: str):
        super().__init__(message)
        self.__n = None
        self.__fi = None
        self.__e = None
        self.__d = None
        self.p = None
        self.q = None


    def __str__(self):
        return f"\033[32mOPENED KEYS:\nE - {self.__e}\nN - {self.__n}\033[0m\n\033[31mCLOSED:\nD - {self.__d}\033[0m"

    def generate_keys(self) -> tuple:
        self.p = number.getPrime(self.__bits_in_keys)
        self.q = number.getPrime(self.__bits_in_keys)
        self.__n = self.p * self.q
        self.__fi = (self.p - 1) * (self.q - 1)
        self.__e = self.__generate_e()
        self.__d = self.find_x(self.__e, 1, self.__fi)

    def encrypt(self) -> List[str]:
        if not (self.__n and self.__e):
            raise KeyError
        res = list()
        for i in self._message:
            tmp = str((self._ALP.index(i) ** self.__e) % self.__n)
            tmp = tmp.rjust(len(str(self.__n)), '0')
            res.append(tmp)
        return res


    def decrypt(self, d: int, n: int) -> any:
        self.__d = d
        self.__n = n
        if isinstance(self._message, str):
            self._message = self._message.split()
        decrypted = [(int(i) ** self.__d) % self.__n for i in self._message]
        if max(decrypted) < len(self._ALP):
            return self._replace_to_char(''.join([self._ALP[int(i)] for i in decrypted]))
        return [(int(i) ** self.__d) % self.__n for i in self._message]

    def set_keys(self, p: int, q: int, e: int) -> None:
        self.p = self.__validate_key(p)
        self.q = self.__validate_key(q)
        self.__n = p * q
        assert self.__n >= len(self._ALP)
        self.__e = self.__validate_e(e, self.__n)

        self.__fi = (self.p - 1) * (self.q - 1)
        self.__d = self.find_x(self.__e, 1, self.__fi)
        assert self.__d != self.__e
        print(f"P - {p}\nQ - {q}\nN = {self.__n}\nE = {self.__e}\nfi(n) = {self.__fi}\nD = {self.__d}")

    def get_keys(self) -> tuple:
        return self.p, self.q, self.__n, self.__e, self.__d, self.__fi


def rsa():
    message = input("Введите сообщение: ")
    choice = int(input("Шифрование - 1, расшифрование - 2"))
    if choice == 1:

        rsa = RSA(message)
        if input("Нужно ли автоматически сгенерировать ключи? y/n").lower() == 'y':
            rsa.generate_keys()
            p, q, n, e, d, fi = rsa.get_keys()
            print(f"Сгенерированные ключи\np = {p}\nq = {q}\nn = {n}\ne = {e}\nd = {d}\nfi = {fi}")
        else:
            p = int(input("Введите p: "))
            q = int(input(f"Введите q: (должна быть больше или равна {int(32 / p) + 1}): "))
            e = int(input(f"Введите e: (должна быть взаимно простая с {(p - 1) * (q - 1)} и 1 < e < {(p - 1) * (q - 1)} ): "))
            rsa.set_keys(p, q, e)
        en = rsa.encrypt()
        print(*en)
    elif choice == 2:
        rsa = RSA(message)
        d = int(getpass.getpass("Введите секретный ключ d: "))
        n = int(input("Введите открытый ключ n: "))
        decrypted = rsa.decrypt(d, n)
        print(decrypted)


if __name__ == "__main__":
    rsa()

