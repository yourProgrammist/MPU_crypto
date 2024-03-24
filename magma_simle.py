PI = [
    [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1],
    [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
    [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
    [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
    [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
    [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
    [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
    [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2]
]


def s_encrypt(in_data):
    for i in range(4):
        first_part_byte = (in_data[i] >> 4) & 0x0f
        sec_part_byte = (in_data[i] & 0x0f)

        in_data[i] = (PI[7 - i * 2][first_part_byte] * 16 + PI[7 - (i * 2 + 1)][sec_part_byte])


def main():
    choice = input("Write 1 for encrypt\n")
    if choice == '1':
        print("Enter key - ")
        key_input = input().strip()
        blk = bytearray.fromhex(key_input)
        s_encrypt(blk)
        print("Encrypted key: ", end="")
        print(''.join(format(x, '02x') for x in blk))


if __name__ == "__main__":
    main()