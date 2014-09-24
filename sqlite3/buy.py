#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: buy.py
#
#        USAGE: ./buy.py
#
#  DESCRIPTION: Buy iPhone Six
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 2014-09-24 14:45:35
#     REVISION: ---
#=========================================================================

import sys
import random
import time
import sqlite3


def buy(consumer=0, count=0):
    """docstring for buy"""

    conn = sqlite3.connect('iphone.db', isolation_level=None)

    bought = 0

    if (count > 0):
        max_try = 10

        while (max_try > 0):
            max_try = max_try - 1

            try:
                with conn as c:
                    cur = c.cursor()

                    # BEGIN, enter critical-session
                    # cur.execute('''BEGIN''')
                    cur.execute('''BEGIN TRANSACTION''')

                    # delay for choice, more time in critical-session
                    time.sleep(0.05)

                    # GET and processing
                    cur.execute('''SELECT total FROM iphone''')
                    old_total = cur.fetchone()[0]

                    new_total = int(old_total) - count

                    # SOLD OUT
                    if (int(new_total) < 0):
                        break

                    # UPDATE and INSERT
                    cur.execute(
                        '''UPDATE iphone SET total = ? WHERE total = ?''', (new_total, old_total))
                    cur.execute(
                        '''INSERT INTO consumer VALUES (?, ?)''', (consumer, count))

                    # COMMIT, leave critical-session
                    cur.execute('''END TRANSACTION''')
                    # cur.execute('''COMMIT''')

                    bought = count
                    break
            except:
                bought = bought - 1
                continue

    if (bought <= 0):
        print(
            "Consumer {:4d} try {:4d} times to buy iPhone Six but got nothing (He needed {:4d})...".format(consumer, abs(bought), count))
    else:
        print(
            "Consumer {:4d} bought {:4d} iPhone Six (He needed {:4d})...".format(consumer, bought, count))


def main():
    """docstring for main"""

    consumer = 0
    sleep = 0
    if (len(sys.argv) > 2):
        consumer = int(sys.argv[1])
        sleep = int(sys.argv[2]) * 1.0

    count = random.randint(1, 9)
    count = random.randint(1, count)

    time.sleep(sleep / 120)
    buy(consumer, count)

if __name__ == '__main__':
    main()
