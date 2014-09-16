#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: inc_with_semaphore.py
#
#        USAGE: ./inc_with_semaphore.py
#
#  DESCRIPTION: Update value with protection (using external sempahore)
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

import posix_ipc


def main():
    """docstring for main"""

    sem = posix_ipc.Semaphore(
        "/sem", flags=posix_ipc.O_CREAT, mode=0600, initial_value=1)

    sem.acquire()

    # beginning of critical session
    with open("/tmp/count", "r+") as f:
        count = f.readline()
        if (count):
            count = int(count) + 1
        else:
            count = 1

        f.seek(0)
        f.truncate()
        f.write(str(count))
    # end of critical session

    sem.release()
    sem.close()

if __name__ == '__main__':
    main()
