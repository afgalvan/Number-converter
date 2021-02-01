from os import system
if __name__ == "__main__":
    print("Ejecutar el archivo main.py")
else:
    from src.curses_actions import *
    from src.converter import *


def show_options(stdscr, current_option):
    options = ("🔥 Decimal -> Binario 🔥", "Binario -> Decimal", "Decimal -> Hex",
               "Hex -> Decimal", "Volver al menú")  # "Binario -> Hex", "Hex -> Binario",

    calculate = 1
    current_option = menu_displayer(
        stdscr, options, "CONVERSION TYPE", current_option)
    if current_option == 0:
        stdscr.clear()
        curses.endwin()
        while calculate:
            calculate = decimal_to_binary()
    elif current_option == 1:
        stdscr.clear()
        curses.endwin()
        while calculate:
            calculate = binary_to_decimal()
    elif current_option == 2:
        stdscr.clear()
        curses.endwin()
        while calculate:
            calculate = decimal_to_hex()
    elif current_option == 3:
        stdscr.clear()
        curses.endwin()
        while calculate:
            calculate = hex_to_decimal()
    elif current_option == len(options)-1:
        stdscr.clear()
        return 0
    show_options(stdscr, current_option)
