#!/usr/bin/env python

import array
import curses
import os
import signal
import sys
import time


def load_maze(path):
    with open(path, 'rb') as fin:
        a = array.array('B')
        a.fromstring(fin.read())
        a = [{0: '@', 255: '.'}[i] for i in a]
        n = int(round(len(a) ** 0.5))
        a = [a[i:i+n] for i in range(0, len(a), n)]
        for i in range(n):
            a[0][i] = a[n-1][i] = "-"
            a[i][0] = a[i][n-1] = '|'
        a[0][0] = a[0][n-1] = a[n-1][0] = a[n-1][n-1] = '+'
        return a


os.chdir(sys.path[0])
MAZE = load_maze('a.raw')
N = len(MAZE)
M = 4
KEY_DIR = {
    curses.KEY_UP:    [-1, 0],
    curses.KEY_DOWN:  [+1, 0],
    curses.KEY_LEFT:  [0, -1],
    curses.KEY_RIGHT: [0, +1]
}


def init(stdscr):
    curses.start_color()
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    stdscr.resize(2 * M + 1, 2 * M + 2)


def get_one_pix(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return ' '
    else:
        return MAZE[x][y]


def show(stdscr, x, y):
    for i in range(2 * M + 1):
        for j in range(2 * M + 1):
            ch = get_one_pix(x - M + i, y - M + j)
            stdscr.addch(i, j, ch)
    stdscr.addch(M, M, 'o', curses.color_pair(1) | curses.A_BOLD)


def main(stdscr):
    signal.alarm(600)
    init(stdscr)
    x, y = N / 2, N / 2
    while True:
        show(stdscr, x, y)
        ch = stdscr.getch()
        dx, dy = KEY_DIR.get(ch, [0, 0])
        nx, ny = x + dx, y + dy
        pix = get_one_pix(nx, ny)
        if pix == '.':
            x, y = nx, ny
    curses.curs_set(0)


if __name__ == '__main__':
    try:
        print "You have 10 minutes to capture the flag :)"
        sys.stdout.write("Loading")
        sys.stdout.flush()
        for i in range(10):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.3)
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
