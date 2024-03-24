from sympy import *
import math

def main():
    gost94()


def gost94():
    message = str(input("Введите ссобщение: ")).upper()
    p = int(input("Введите параметр p - большое простое число: ")) #Вводим ключ p
    while not (isprime(p)):
        p = int(input("Вы ввели не простое число. Повторите ввод: "))
    q = int(input("Введите параметр q - простой сомножитель числа p-1: ")) #Вводим ключ q
    while not (isprime(q)):
        q = int(input("Вы ввели не простое число. Повторите ввод: "))
    k = 0
    for i in range(2, q // 2 + 1):
        if (q % i == 0):
            k = k + 1
    if (p-1) % q != 0 and (q>0):
        q = int(input("Введите параметр q - простой сомножитель числа p-1: "))  #Проверка q
    a = int(input("Введите параметр a - число в пределах 1<a<p-1: ")) #Вводим ключ a
    Z = (a**q) % p
    while not ((Z == 1) and (a<p-1) and (a > 1)):
        a = int(input("Ввод не прошёл условия. Повторите попытку: "))  # Вводим ключ a
        Z = (a ** q) % p
    x = int(input("Введите параметр x - число меньшее q: ")) #Вводим ключ x
    if not (x<q):
        x = int(input("Ввод не прошёл условия. Повторите попытку: "))  # Вводим ключ x
    y = a**x % p
    print("Расчитанный параметр y: ", y)
    k = int(input("Введите случайное число k, меньшее q: ")) #Вводим ключ k
    if not (k<q):
        k = int(input("Ввод не прошёл условия. Повторите попытку: "))  # Вводим ключ k
    m = hash(message)
    print("Хеш: ",m)
    array_return = find_digital_signature(a,k,p,q,m,x)
    while (array_return[0] == 0 or array_return[1] == 0):
        k = int(input("Параметр s или r равен 0. Введите другое случаное число k<q: "))  # Вводим ключ k
        while not (k < q):
            k = int(input("Ввод не прошёл условия. Повторите попытку: "))  # Вводим ключ k
        array_return = find_digital_signature(a,k,p,q,m,x)
    r = array_return[0]
    s = array_return[1]
    print("Цифровая подпись (r;s): ", r, s)
    v = m**(q-2) % q
    print("v:",v)
    z1 = (s*v) % q
    print("z1:",z1)
    z2 = ((q-r)*v) % q
    print("z2:",z2)
    u = (((a**z1)*(y**z2)) % p) % q
    print("u: ", u)
    if u == r:
        print("u=r. Подпись верна.")


def find_digital_signature(a,k,p,q,m,x):
    r = (a**k % p) % q
    if m % q == 0:
        m = 1
    s = (x*r + k*m) % q
    return [r,s]

def hash(message):
    alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ,.!?;:&{}[]—«»\'\"-–1234 …'
    p = 11
    h = 0 #Начальное значение хэша
    for i in range(len(message)):
        h = (h + (alphabet.index(message[i])+1))**2 % p #Вычисление
    return h



def solve_linear_congruence(a, b, m): #Функция для решения модульных сравненений
    g = math.gcd(a, m) #НОД a и m
    if b % g:
        raise ValueError("No solutions")
    a, b, m = a//g, b//g, m//g
    return pow(a, -1, m) * b % m #вычисление

if __name__ == "__main__":
    main()
