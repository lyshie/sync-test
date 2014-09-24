#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: get.py
#
#        USAGE: ./get.py
#
#  DESCRIPTION: Get current values
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 2014-09-24 14:46:24
#     REVISION: ---
#=========================================================================

import sqlite3


def main():
    """docstring for main"""

    conn = sqlite3.connect('iphone.db')

    with conn as c:
        c.row_factory = sqlite3.Row
        cur = c.cursor()

        # total
        cur.execute('''SELECT total FROM iphone''')
        for row in cur:
            print("   TOTAL: {}".format(row['total']))

        # detail information
        sold = 0
        cur.execute('''SELECT id, count FROM consumer ORDER BY id ASC''')
        for row in cur:
            print("\t{:4d} => {:4d}".format(row['id'], row['count']))
            sold = sold + row['count']

        # total sold
        print("    SOLD: {}".format(sold))


if __name__ == '__main__':
    main()
