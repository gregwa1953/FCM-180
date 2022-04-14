#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     curses1a.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue # 180
# Written by G.D. Walters
# Copyright (c) 2022 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
import curses


def centre(strng):
    global num_cols
    strlen = len(strng)
    return int((num_cols / 2) - (strlen / 2))


screen = curses.initscr()
curses.start_color()
global num_rows, num_cols
num_rows, num_cols = screen.getmaxyx()
print(num_rows, num_cols)
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
strn = 'Welcome to Full Circle Magazine #180'
screen.addstr(0, centre(strn), strn,
              curses.color_pair(1))  # | curses.A_BOLD | curses.A_UNDERLINE)
strn2 = 'This is the last line of the terminal'
screen.addstr(num_rows - 1, centre(strn2), strn2,
              curses.color_pair(2) | curses.A_BOLD | curses.A_UNDERLINE)
# ===================================================
# Show the different attributes...
# ===================================================
screen.addstr(3, 2, "Curses Screen Attributes")
screen.addstr(4, 2, "=" * 20)
screen.addstr(5, 2, "This is A_BLINK", curses.A_BLINK)
screen.addstr(6, 2, "This is A_BOLD", curses.A_BOLD)
screen.addstr(7, 2, "This is A_DIM", curses.A_DIM)
screen.addstr(8, 2, "This is A_REVERSE", curses.A_REVERSE)
screen.addstr(9, 2, "This is A_STANDOUT", curses.A_STANDOUT)
screen.addstr(10, 2, "This is A_UNDERLINE", curses.A_UNDERLINE)
strng = "Press a key to end demo..."
screen.addstr(num_rows - 3, centre(strng), strng, curses.A_BLINK)
screen.refresh()
c = screen.getch()
curses.endwin()
