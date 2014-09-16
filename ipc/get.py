#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: get.py
#
#        USAGE: ./get.py
#
#  DESCRIPTION: Get current value in the file
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
    with open("/tmp/count", "r") as f:
        count = f.readline()
        print(count)

if __name__ == '__main__':
    main()
