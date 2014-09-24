#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: clear.py
#
#        USAGE: ./clear.py
#
#  DESCRIPTION: Set initial vaules
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 2014-09-24 14:45:22
#     REVISION: ---
#=========================================================================

import sqlite3


def main():
    """docstring for main"""

    sql_command = '''
        DROP TABLE IF EXISTS iphone;

        CREATE TABLE IF NOT EXISTS iphone (
            total INTEGER
        );

        DELETE FROM iphone;

        DROP TABLE IF EXISTS consumer;

        CREATE TABLE IF NOT EXISTS consumer (
            id    INTEGER, 
            count INTEGER
        );

        DELETE FROM consumer;
    '''

    conn = sqlite3.connect('iphone.db')

    with conn as c:
        c.executescript(sql_command)
        c.execute('''INSERT OR REPLACE INTO iphone VALUES (?)''', (100, ))

if __name__ == '__main__':
    main()
