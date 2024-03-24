from atbash import atbash
from ceaser import ceaser
from polibiy import polibiy
from tritemiy import tritemiy
from belazo import belazo
from vizener import vizener
from s_block import s_block
from matrix import matrix
from playfair import playfair
from virtical import vertical
from cardano import cardano
from network import network
from shenon import shenon
from gamma_magma import gamma_magma
from a51 import a51
from magma import magma
from kuznechik import kuznechik
from rsa import rsa
from elgamal import elgamal
from rsa_cp import rsa_cp
from ghost94 import gost94
from deffie import key_exchange
GUEST_MESSAGE = """
Выберите криптографический алгоритм:
1\t-\tЩифр Атбаш
2\t-\tШифр Цезаря
3\t-\tКвадрат Полибия
4\t-\tШифр Тритемия
5\t-\tШифр Белазо
6\t-\tШифр Виженера
7\t-\tS-блок замены ГОСТ Р 34.12-2015 («МАГМА»)
8\t-\tМатричный шифр
9\t-\tШифр Плэйфера
10\t-\tВертикальная перестановка
11\t-\tРешетка Кардано
12\t-\tПерестановка в комбинационных шифрах (DES, МАГМА)
13\t-\tОдноразовый блокнот К.Шеннона
14\t-\tГаммирование ГОСТ 28147-89 и ГОСТ Р 34.13-2015 (ГОСТ Р 34.12-2015 «Магма»)
15\t-\tА5 /1
16\t-\tМАГМА
17\t-\tКУЗНЕЧИК
18\t-\tRSA
19\t-\tElgamal
20\t-\tЦП RSA
21\t-\tГОСТ Р 34.10-94
22\t-\tОБМЕН КЛЮЧАМИ ПО ДИФФИ-ХЕЛЛМАНУ
"""

if __name__ == '__main__':
    choice = int(input(GUEST_MESSAGE))
    if choice == 1:
        atbash()
    elif choice == 2:
        ceaser()
    elif choice == 3:
        polibiy()
    elif choice == 4:
        tritemiy()
    elif choice == 5:
        belazo()
    elif choice == 6:
        vizener()
    elif choice == 7:
        s_block()
    elif choice == 8:
        matrix()
    elif choice == 9:
        playfair()
    elif choice == 10:
        vertical()
    elif choice == 11:
        cardano()
    elif choice == 12:
        network()
    elif choice == 13:
        shenon()
    elif choice == 14:
        gamma_magma()
    elif choice == 15:
        a51()
    elif choice == 16:
        magma()
    elif choice == 17:
        kuznechik()
    elif choice == 18:
        rsa()
    elif choice == 19:
        elgamal()
    elif choice == 20:
        rsa_cp()
    elif choice == 21:
        gost94()
    elif choice == 22:
        key_exchange()






