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
#      CREATED: 2014-09-24 10:06:24
#     REVISION: ---
#=========================================================================

import redis


def verify_and_show(r):
    """docstring for verify_and_show"""

    r_total = r.get('sync-test:total')
    r_consumer = r.get('sync-test:consumer')
    r_count = r.get('sync-test:count')

    # summary
    print("   TOTAL: {}".format(r_total))
    print("CONSUMER: {}".format(r_consumer))
    print("   COUNT: {}".format(r_count))

    # detail infomation
    print("  DETAIL:")

    consumers = r_consumer.split(",")
    counts = r_count.split(",")

    sold = 0
    for a, b in zip(consumers, counts):
        if ("" != a):
            print("\t{:>4s} => {:>4s}".format(a, b))
            sold = sold + int(b)

    # total sold
    print("    SOLD: {}".format(sold))


def main():
    """docstring for main"""
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    verify_and_show(r)

if __name__ == '__main__':
    main()
