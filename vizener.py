RUSSIAN_ALP = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
SIZE_ALP = 32
SIZE_BUFFER = 20000

ERROR_ALP = 0
ERROR_CHOICE = 1
ERROR_KEY = 2
OK = 0
FAILURE = 1

def index_letter(ch):
    for i, letter in enumerate(RUSSIAN_ALP):
        if ch == letter:
            return i
    return -1

def encode(input_str, key, choice):
    output_str = ""
    prev = None
    for ch in input_str:
        k = index_letter(ch)
        if prev is None:
            m = index_letter(key)
        else:
            m = prev
        if choice == '1':
            prev = k
        if k != -1:
            if choice == '1':
                output_str += RUSSIAN_ALP[(m + k) % SIZE_ALP]
            elif choice == '2':
                output_str += RUSSIAN_ALP[(k - m + SIZE_ALP) % SIZE_ALP]
                prev = (k - m + SIZE_ALP) % SIZE_ALP
        else:
            exit(ERROR_ALP)
    return output_str

def to_standard_message(input_str):
    output_str = ""
    for ch in input_str:
        if ch == ',':
            output_str += "зпт"
        elif ch == '.':
            output_str += "тчк"
        elif ch == 'ё':
            output_str += "е"
        elif ch == ' ':
            output_str += "прб"
        elif ch.lower() in RUSSIAN_ALP:
            output_str += ch.lower()
    return output_str

def from_standard_message(input_str):
    output_str = ""
    i = 0
    while i < len(input_str):
        if i + 2 < len(input_str) and input_str[i:i+3] == "зпт":
            output_str += ","
            i += 3
        elif i + 2 < len(input_str) and input_str[i:i+3] == "тчк":
            output_str += "."
            i += 3
        elif i + 2 < len(input_str) and input_str[i:i+3] == "прб":
            output_str += " "
            i += 3
        else:
            output_str += input_str[i]
            i += 1
    return output_str

def vizener():
    print("Введите 1 для шифрования, 2 для дешифрования")
    choice = input().strip()
    if choice not in ['1', '2']:
        exit(ERROR_CHOICE)
    
    print("Введите ключ - ", end="")
    key = input().strip()
    
    print("Введите сообщение - ", end="")
    input_str = input().strip()
    
    if choice == '1':
        input_str = to_standard_message(input_str)
        output_str = encode(input_str, key, choice)
        print("Зашифрованное сообщение -", output_str)
    elif choice == '2':
        output_str = encode(input_str, key, choice)
        output_str = from_standard_message(output_str)
        print("Расшифрованное сообщение -", output_str)

if __name__ == "__main__":
    vizener()
