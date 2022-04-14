#!/usr/bin/env python
# CursesExample1
#-------------------------------
# Curses Programming Sample 1
#-------------------------------
import curses
myscreen = curses.initscr()
myscreen.border(0)
myscreen.addstr(12, 25, "See Curses, See Curses Run!")
myscreen.refresh()
myscreen.getch()
curses.endwin()