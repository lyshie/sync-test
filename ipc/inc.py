#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: inc.py
#
#        USAGE: ./inc.py
#
#  DESCRIPTION: Update the value without protection
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 2014-09-16 16:19:24
#     REVISION: ---
#=========================================================================


def main():
    """docstring for main"""

    with open("/tmp/count", "r+") as f:
        count = f.readline()
        if (count):
            count = int(count) + 1
        else:
            count = 1

        f.seek(0)
        f.truncate()
        f.write(str(count))

if __name__ == '__main__':
    main()
