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
#      CREATED: 2014-09-24 10:08:35
#     REVISION: ---
#=========================================================================

import sys
import random
import time
import redis


def buy(r, consumer=0, count=0):
    """docstring for buy"""

    bought = 0

    if (count > 0):
        max_try = 10

        with r.pipeline() as pipe:
            while (max_try > 0):
                max_try = max_try - 1

                try:
                    # WATCH, enter critical-session
                    pipe.watch('sync-test:total')
                    pipe.watch('sync-test:consumer')
                    pipe.watch('sync-test:count')

                    # delay for choice, more time in critical-session
                    time.sleep(0.01)

                    # GET and processing
                    r_total = pipe.get('sync-test:total')
                    r_consumer = pipe.get('sync-test:consumer')
                    r_count = pipe.get('sync-test:count')

                    r_total = int(r_total) - count
                    r_consumer = r_consumer + "{},".format(consumer)
                    r_count = r_count + "{},".format(count)

                    # SOLD OUT
                    if (int(r_total) < 0):
                        break

                    # MULTI and SET
                    pipe.multi()
                    pipe.set('sync-test:total', r_total)
                    pipe.set('sync-test:consumer', r_consumer)
                    pipe.set('sync-test:count', r_count)

                    # EXECUTE, leave critical-session
                    pipe.execute()
                    bought = count
                    break
                except redis.WatchError:
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
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    consumer = 0
    sleep = 0
    if (len(sys.argv) > 2):
        consumer = int(sys.argv[1])
        sleep = int(sys.argv[2]) * 1.0

    count = random.randint(1, 6)
    count = random.randint(1, count)

    time.sleep(sleep / 70)
    buy(r, consumer, count)

if __name__ == '__main__':
    main()
