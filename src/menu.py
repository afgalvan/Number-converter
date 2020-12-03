from time import sleep
import curses


if __name__ == "__main__":
    print("Ejecutar el archivo main.py")
else:
    from src.curses_actions import *
    from src.menu_conversions import show_options
    from src.credits import more_info
    from src.exit_menu import exit_menu


def main_menu(stdscr, current_option):
    options = ("Convertir números", "Más información", "Salir")

    current_option = menu_displayer(
        stdscr, options, "NUMBER CONVERTER", current_option)
    if current_option == 0:
        show_options(stdscr, 0)
    elif current_option == 1:
        more_info(stdscr, 0)
    else:
        exit_menu(stdscr)
    main_menu(stdscr, current_option)


def menu(stdscr):
    set_size(stdscr)
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    main_menu(stdscr, 0)


def main():
    curses.wrapper(menu)
