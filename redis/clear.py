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
#      CREATED: 2014-09-24 10:05:21
#     REVISION: ---
#=========================================================================

import redis


def main():
    """docstring for main"""
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    r.set("sync-test:total", 30)
    r.set("sync-test:consumer", "")
    r.set("sync-test:count", "")

if __name__ == '__main__':
    main()
