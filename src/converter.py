from time import time
from subprocess import call
try:
    from src.controllers.controllers import *
except:
    from controllers.controllers import *
if OS == "Windows":
    from msvcrt import getche, getch
else:
    # from getch import getche, getch
    pass


def decimal2binary():
    clear()
    center_print("DECIMAL A BINARIO", 5)
    decimal = ask_value(8)

    x_position = 2
    y_position = 10
    binary_list = []
    while decimal > 1:
        gotoxy(x_position, y_position)
        operation = f"{decimal} │ 2"
        print(operation)
        y_position += 1

        bin_digit = decimal % 2
        spaces = len(str(decimal))
        decimal //= 2
        gotoxy(x_position, y_position)
        print("{0}{1}└───┐".format(bin_digit, " " * spaces))
        binary_list.append(bin_digit)

        y_position += 1
        x_position += 4
    gotoxy(x_position, y_position)
    print(1)

    center_print("Número binario.", y_position+2)
    binary_list.append(1)
    binary_number = ""
    for n in binary_list[::-1]:
        binary_number += str(n)
    center_print(binary_number, y_position+3)
    print()

    getch()
    clear()


def binary2decimal():
    clear()
    center_print("BINARIO A DECIMAL", 5)
    binary = ask_value(8)

    y_position = 10
    decimal_number = 0
    for power, n in enumerate(str(binary)):
        power_result = 2 ** power
        dec_acumulator = int(n) * power_result
        decimal_number += dec_acumulator
        operation = f"{n} x 2 ^{power} = {n} x {power_result} = {dec_acumulator}"
        center_print(operation, y_position)
        y_position += 1

    bar = "─" * (len(str(decimal_number)) * 2)
    center_print(bar, y_position)
    center_print(str(decimal_number), y_position + 1)
    print()
    getch()
    clear()


if __name__ == "__main__":
    binary2decimal()
