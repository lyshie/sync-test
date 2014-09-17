#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: client.py
#
#        USAGE: ./client.py
#
#  DESCRIPTION: A client to invoke 'INC' command (inc)
#
#      OPTIONS: ---
# REQUIREMENTS: ---
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: SHIE, Li-Yi (lyshie), lyshie@mx.nthu.edu.tw
# ORGANIZATION:
#      VERSION: 1.0
#      CREATED: 2014-09-17 15:16:30
#     REVISION: ---
#=========================================================================

import socket


def exec_and_fetch(socket, command):
    """docstring for exec_and_fetch"""
    socket.sendall(command)
    ret = socket.recv(1024)

    return ret


def main():
    """docstring for main"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 9999))

    result = exec_and_fetch(s, "INC")
    exec_and_fetch(s, "QUIT")

    s.close()

    print(result)


if __name__ == '__main__':
    main()
