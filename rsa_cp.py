import math

def rsa_cp():
    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))
    message = input("Введите сообщение: ").replace(" ", "").replace(".", 'тчк').replace("-", '').replace('ё', 'е').lower()
    n = p * q
    print("N: ", n)
    fn = (p - 1) * (q - 1)
    e = int(input("Введите просто число E, взаимно простое с функцией Эйлера по N ") + str(fn) + ": ")
    while math.gcd(e, fn) != 1:
        e = int(input("Ошибка! Числа не взаимно простое. Введите просто число E, взаимно простое с функцией Эйлера по N ") + str(fn) + ": ")
    d = solve_module_diff(e, 1, fn)
    print("Вычисленный ключ D: ", d)
    hashed_message = hash(message)
    print("Хэш сообщения: ", hashed_message)
    s = pow(hashed_message, d, n)
    print("Подпись", s)
    m = pow(s, e, n)
    if m == hashed_message:
        print("Подпись верна")
    else:
        print("Подпись неверна")

def solve_module_diff(a, b, m):
    g = math.gcd(a, m)
    if b % g:
        raise Exception("NO solution")
    a //= g
    b //= g
    m //= g
    return pow(a, -1, m) * b % m

def hash(message):
    alp = "qабвгдежзийклмнопрстуфхцчшщъыьэюя"
    h = 0
    p = 47
    for i in message:
        h = (h + alp.index(i)) ** 2 % p
    if h == 0:
        return 1
    return h

if __name__ == "__main__":
    rsa_cp()