#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: clear.py
#
#        USAGE: ./clear.py
#
#  DESCRIPTION: Destroy the semaphore and clear the file
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
    sem.unlink()

    with open("/tmp/count", "w") as f:
        f.write("0")

if __name__ == '__main__':
    main()
