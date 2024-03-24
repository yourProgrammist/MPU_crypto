RUSSIAN_ALP = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
SIZE_ALP = 32
ERROR_ALP = -1
ERROR_CHOICE = -2

# Получение позиции буквы в алфавите
def index_letter(ch):
    code = -1
    for i, letter in enumerate(RUSSIAN_ALP):
        if ch == letter:
            code = i
            break
    return code

# Алгоритм шифрование/расшифрования
def encode(input_string):
    result = ""
    for ch in input_string:
        k = index_letter(ch)
        if k != -1:
            result += RUSSIAN_ALP[SIZE_ALP - 1 - k]
        else:
            exit(ERROR_ALP)
    return result

# Функция, которая переводит спец-символы в комбинацию обычных символов, заглавные буквы в прописные
def to_standart_message(input_string):
    output = ""
    for ch in input_string:
        if ch == ',':
            output += "зпт"
        elif ch == '.':
            output += "тчк"
        elif ch == 'ё':
            output += "е"
        elif index_letter(ch.lower()) != -1:
            output += ch.lower()
    return output

# Функция, которая переводит комбинации символов тчк зпт в . и , соответсвенно
def from_standart_message(input_string):
    output = ""
    i = 0
    while i < len(input_string):
        if i + 2 < len(input_string) and input_string[i:i+3] == 'зпт':
            output += ","
            i += 3
        elif i + 2 < len(input_string) and input_string[i:i+3] == 'тчк':
            output += "."
            i += 3
        else:
            output += input_string[i]
            i += 1
    return output

def atbash():
    choice = input("Введите 1 для шифрования, 2 для расшифрования\n")
    BUFFER = input("Введите сообщение").strip()
    OUTPUT = ""

    if choice == '1':
        OUTPUT = to_standart_message(BUFFER)
        OUTPUT = encode(OUTPUT)
        print("Зашифрованное сообщение -", OUTPUT)
    elif choice == '2':
        OUTPUT = encode(BUFFER)
        OUTPUT = from_standart_message(OUTPUT)
        print("Расшифрованное сообщение -", OUTPUT)
    else:
        exit(ERROR_CHOICE)

if __name__ == "__main__":
    atbash()
