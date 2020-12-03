from time import time
from subprocess import call
from re import fullmatch
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
    decimal = ask_value(8, int)

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
    while True:
        binary = ask_value(8, int)
        if fullmatch("[01]+", str(binary)):
            break
        error_print("Sólo ingrese 1-0", "c", 10)
        clear_input(23, 8)

    y_position = 10
    decimal_number = 0
    for power, n in enumerate(str(binary)[::-1]):
        power_result = 2 ** power
        dec_acumulator = int(n) * power_result
        decimal_number += dec_acumulator
        operation = f"{n} x 2 ^{power} = {n} x {power_result} = {dec_acumulator}"
        center_print(operation, y_position)
        y_position += 1

    bar = "─" * (len(str(decimal_number)) + 2)
    center_print(bar, y_position)
    center_print(str(decimal_number), y_position + 1)
    print()
    getch()
    clear()


def decimal2hex():
    clear()
    center_print("DECIMAL A HEXADECIMAL", 5)
    decimal = ask_value(8, int)

    x_position = 2
    y_position = 10
    hexadecimal_list = []
    while decimal > 1:
        gotoxy(x_position, y_position)
        operation = f"{decimal} │ 16"
        print(operation)
        y_position += 1

        hex_digit = decimal % 16
        spaces = len(str(decimal))
        decimal //= 16
        gotoxy(x_position, y_position)
        print("{0}{1}└──┐".format(hex_digit, " " * spaces))
        hexadecimal_list.append(hex_digit)

        y_position += 1
        x_position += 4
    gotoxy(x_position, y_position)
    print(decimal)
    hexadecimal_list.append(decimal)

    center_print("Número hexadecimal.", y_position+2)
    hexadecimal_number = ""
    specials_hex = {"10": "A", "11": "B", "12": "C",
                    "13": "D", "14": "E", "15": "F"}
    for n in hexadecimal_list[::-1]:
        if n < 1:
            continue
        if n >= 10:
            hexadecimal_number += specials_hex[str(n)]
            continue
        hexadecimal_number += str(n)
    center_print(hexadecimal_number, y_position+3)
    print()

    getch()
    clear()


def hex2decimal():
    clear()
    center_print("HEXADECIMAL A DECIMAL", 5)
    while True:
        hexadecimal = ask_value(8, str)
        if fullmatch("[0-9ABCDEF]+", str(hexadecimal)):
            break
        error_print("Sólo ingrese 1-0", "c", 10)
        clear_input(23, 8)

    y_position = 10
    decimal_number = 0
    for power, n in enumerate(str(hexadecimal)[::-1]):
        power_result = 16 ** power
        hex_acumulator = int(n) * power_result
        decimal_number += hex_acumulator
        operation = f"{n} x 2 ^{power} = {n} x {power_result} = {hex_acumulator}"
        center_print(operation, y_position)
        y_position += 1

    bar = "─" * (len(str(decimal_number)) + 2)
    center_print(bar, y_position)
    center_print(str(decimal_number), y_position + 1)
    print()
    getch()
    clear()


if __name__ == "__main__":
    decimal2hex()
