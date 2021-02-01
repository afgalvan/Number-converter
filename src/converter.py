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
    from getch import getche, getch
    pass


def keep_doing():
    print("\n\nEsc para salir...")
    key_pressed = ord(getch())
    clear()
    if key_pressed == 27:
        return 0
    return 1


def convert_by_division(base: int):
    decimal = ask_value(8, int)

    y_position = 10
    converted_list = []
    spaces = len(str(decimal))
    while decimal >= 1:
        binary_digit = decimal % base
        converted_list.append(binary_digit)

        operation = f"{decimal:>{spaces}} │ {base} -> {binary_digit}"
        center_print(operation, y_position)
        y_position += 1

        decimal //= base

    return converted_list[::-1], y_position


def convert_by_multiplication(iterable, base: int):
    y_position = 10
    decimal_number = 0
    for power, n in enumerate(iterable[::-1]):
        power_result = base ** power
        dec_acumulator = int(n) * power_result
        decimal_number += dec_acumulator
        operation = f"{n} x {base}^{power} = {n} x {power_result} = {dec_acumulator}"
        center_print(operation, y_position)
        y_position += 1

    bar = "─" * (len(str(decimal_number)) + 2)
    center_print(bar, y_position)
    center_print(str(decimal_number), y_position + 1)


def decimal_to_binary():
    clear()
    center_print("DECIMAL A BINARIO", 5)
    binary_base = 2
    binary_list, y_position = convert_by_division(binary_base)

    binary_number = "".join([str(n) for n in binary_list])

    center_print("Número binario.", y_position+2)
    center_print(binary_number, y_position+3)

    return keep_doing()


def decimal_to_hex():
    clear()
    center_print("DECIMAL A HEXADECIMAL", 5)
    hexadecimal_base = 16
    hexadecimal_list, y_position = convert_by_division(hexadecimal_base)

    specials_hex = {"10": "A", "11": "B", "12": "C",
                    "13": "D", "14": "E", "15": "F"}

    center_print("Número hexadecimal.", y_position+2)
    hexadecimal_number = "".join([str(n) if n < 10 else specials_hex[str(n)]
                                  for n in hexadecimal_list])
    center_print(hexadecimal_number, y_position+3)

    return keep_doing()


def binary_to_decimal():
    clear()
    center_print("BINARIO A DECIMAL", 5)
    while True:
        binary = ask_value(8, int)
        if fullmatch("[01]+", str(binary)):
            break
        error_print("Sólo ingrese 1-0", "c", 10)
        clear_input(23, 8)

    binary = str(binary)
    binary_base = 2
    convert_by_multiplication(binary, binary_base)

    return keep_doing()


def hex_to_decimal():
    clear()
    center_print("HEXADECIMAL A DECIMAL", 5)
    while True:
        hexadecimal = ask_value(8).upper()
        if fullmatch("[0-9ABCDEF]+", str(hexadecimal)):
            break
        error_print("Valores inválidos.", "c", 10)
        clear_input(23, 8)

    specials_hex = {"A": "10", "B": "11", "C": "12",
                    "D": "13", "E": "14", "F": "15"}

    hexa_list = [value for value in hexadecimal]
    hexa_list = [specials_hex[n] if not n.isdigit() else n for n in hexa_list]

    hexa_base = 16
    convert_by_multiplication(hexa_list, hexa_base)

    return keep_doing()


def hex_to_binary():
    hex_to_decimal()


if __name__ == "__main__":
    hex_to_decimal()
