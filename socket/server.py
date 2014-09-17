#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=========================================================================
#
#         FILE: server.py
#
#        USAGE: ./server.py
#
#  DESCRIPTION: A socket server to increment value with/without lock protection
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

import signal
import SocketServer
import threading
import time


class Increment(object):

    """docstring for Increment"""

    def __init__(self, init_value=0):
        """docstring for __init__"""
        super(Increment, self).__init__()
        self.val = init_value
        self.lock = threading.Lock()

    def inc(self):
        """docstring for inc"""
        old = self.get()
        time.sleep(0.001)
        new = old + 1
        self.set(new)
        return new

    def lock_inc(self):
        """docstring for lock_inc"""
        self.lock.acquire()

        old = self.get()
        time.sleep(0.001)
        new = old + 1
        self.set(new)

        self.lock.release()
        return new

    def get(self):
        """docstring for get"""
        return self.val

    def set(self, value):
        """docstring for set"""
        self.val = value
        return self.val


class NumberTCPHandler(SocketServer.BaseRequestHandler):

    """docstring for NumberTCPHandler"""

    def handle(self):
        """docstring for handle"""
        while True:
            data = self.request.recv(1024).strip()

            if (len(data) == 0):
                self.finish()
                break

            if (data.upper() == "GET"):
                self.response(str(self.server.increment.get()) + "\n")
            elif (data.upper() == "INC"):
                self.response(str(self.server.increment.inc()) + "\n")
            elif (data.upper() == "LINC"):
                self.response(str(self.server.increment.lock_inc()) + "\n")
            elif (data.upper().startswith("SET")):
                try:
                    cmd, val = data.upper().split()
                    self.response(
                        str(self.server.increment.set(int(val))) + "\n")
                except:
                    pass
            elif (data.upper() == "QUIT"):
                self.finish()
                break

    def response(self, data):
        """docstring for response"""
        try:
            self.request.send(str(self.server.increment.get()) + "\n")
        except:
            pass


class TCPNumberServer(SocketServer.ThreadingTCPServer):

    """docstring for TCPNumberServer"""

    def __init__(self, server_address, handler_class=NumberTCPHandler):
        """docstring for __init__"""
        self.increment = Increment(0)
        self.allow_reuse_address = True
        self.daemon_threads = True
        SocketServer.TCPServer.__init__(self, server_address, handler_class)


class IntHandler():

    def __init__(self, server=None, cv=None):
        """docstring for __init__"""
        self.s_thread = None
        if (server):
            self.server = server
        if (cv):
            self.cv = cv

    def handle(self, signum, frame):
        """docstring for handle"""
        if (not self.s_thread):
            self.s_thread = threading.Thread(target=self.shutdown)
            self.s_thread.start()

    def shutdown(self):
        """docstring for shutdown"""
        print("Shutdown thread: {}".format(
            threading.currentThread().getName()))

        if (self.server):
            self.server.shutdown()

        if (self.cv):
            self.cv.set()


def main():
    """docstring for main"""
    print("Server thread: {}".format(threading.currentThread().getName()))
    cv = threading.Event()

    HOST, PORT = "127.0.0.1", 9999

    server = TCPNumberServer((HOST, PORT), NumberTCPHandler)

    int_handler = IntHandler(server, cv)
    signal.signal(signal.SIGINT, int_handler.handle)

    server.serve_forever()
    cv.wait()

if __name__ == '__main__':
    main()
