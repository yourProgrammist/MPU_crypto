def key_exchange():
    n = int(input("Введите число n: "))
    a = int(input("Введите число a, меньшее n: "))
    while not 1 < a < n:
        a = int(input("a должно быть меньше n! Повторите ввод параметра a: "))
    Ka = int(input("Введите секретный ключ Ka: "))
    Kb = int(input("Введите секретный ключ Kb: "))
    while not (Ka > 1 and Ka < n):
        Ka = int(input("Ka должен быть в интервале (1;n)! Повторите ввод: "))
    while not (Kb > 1 and Kb < n):
        Kb = int(input("Kb должен быть в интервале (1;n)! Повторите ввод: "))
    Ya = a**Ka % n
    Yb = a**Kb % n

    K1 = Yb**Ka % n
    K2 = Ya**Kb % n

    if K1 == 1 or K2 == 1:
        print("Секретные ключи равны единице, повторите ввод!")
        return key_exchange()

    print("Секретный ключ K1: ", K1)
    print("Секретный ключ K2: ", K2)
    if K1 == K2:
        print("Общий секретный ключ: ", K1)
    else:
        print("Возникла ошибка")


if __name__ == "__main__":
    key_exchange()