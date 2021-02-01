from time import sleep
import curses
from webbrowser import open as open_url
if __name__ == "__main__":
    print("Ejecutar el archivo main.py")
else:
    from src.curses_actions import *

credits_text = """Hecho por Andrés Galván

Con la colaboración de
Javier Guerra

Copyright (C) 2020 by Andrés Galván
"""


def more_info(stdscr, current_option):
    URL = "https://github.com/afgalvan"
    options = ("Créditos", "Github", "Licencia", "Volver al menú")

    current_option = menu_displayer(
        stdscr, options, "MÁS INFORMACIÓN", current_option)
    if current_option == 0:
        show_credits(stdscr)
    elif current_option == 1:
        open_url(URL)
    elif current_option == 2:
        show_license(stdscr)
    else:
        stdscr.clear()
        return 0
    more_info(stdscr, current_option)


def show_credits(stdscr):
    h, w = stdscr.getmaxyx()
    credits_list = credits_text.split("\n")
    space_diff = 2
    diff_limit = len(credits_list) + 1
    last_line = 3 - len(credits_list)

    curses.curs_set(0)
    y = h-1
    while y >= last_line:
        stdscr.clear()
        for line in credits_list:
            if y + 1 > h:
                break
            if y - 2 < 1:
                y += 1
                continue
            center_print(stdscr, line, y)
            y += 1
        sleep(0.4)
        y -= space_diff
        if space_diff < diff_limit:
            space_diff += 1


def show_license(stdscr):
    license_text = """MIT License

Copyright (c) 2020 Andrés Galván

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    stdscr.clear()
    license_list = license_text.split("\n")
    h, w = stdscr.getmaxyx()
    row = h//2 - len(license_list)//2
    for y, line in enumerate(license_list):
        center_print(stdscr, line, row + y)
    stdscr.getch()
