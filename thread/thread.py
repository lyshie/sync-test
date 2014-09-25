#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import random
import time


class Pocket(object):

    """docstring for Pocket"""

    def __init__(self, left=0, right=30, lock=None):
        super(Pocket, self).__init__()
        self.left = left
        self.right = right
        self.total = self.left + self.right
        self.lock = lock
        self.cs_sleep = 0.000001

    def to_right(self, amount=0):
        """docstring for toRight"""
        if (self.lock):
            self.lock.acquire()

        self.left = self.left - amount
        time.sleep(self.cs_sleep)
        self.right = self.right + amount

        if (self.lock):
            self.lock.release()

    def to_left(self, amount=0):
        """docstring for to_left"""
        if (self.lock):
            self.lock.acquire()

        self.right = self.right - amount
        time.sleep(self.cs_sleep)
        self.left = self.left + amount

        if (self.lock):
            self.lock.release()

    def is_ok(self):
        """docstring for is_ok"""
        if (self.left + self.right == self.total):
            return True
        else:
            return False

    def show(self, display=True):
        """docstring for show"""
        msg = "Total = {:4d}, Result = {:4d}, Left = {:4d}, Right = {:4d}".format(
            self.total, self.left + self.right, self.left, self.right)

        if (display):
            print(msg)
        else:
            return msg


def change(pocket=None, low=-10, up=10):
    """docstring for change"""
    if (pocket):
        for c in xrange(100):
            amount = random.randint(low, up)
            pocket.to_left(amount)


def main():
    """docstring for main"""

    lock = None
    if (len(sys.argv) > 1):
        lock = threading.Lock()

    pocket = Pocket(lock=lock)
    for i in xrange(30):
        t = threading.Thread(target=change, args=(pocket, ))
        t.setDaemon(True)
        t.start()

    main_thread = threading.currentThread()

    for t in threading.enumerate():
        if (t is main_thread):
            continue
        t.join()

    print("Correct = {:>5s}, {}".format(
        str(pocket.is_ok()), pocket.show(display=False)))


if __name__ == '__main__':
    main()
