#!/usr/bin/env python3

import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
run = False

def receive(s):
    global run
    while run:
        data = s.recv(4096)
        newlinesplt = data.decode("utf8").split("\\n")
        runs = 0
        for i in newlinesplt:
            print (newlinesplt[runs])
            runs += 1
            if runs == len(newlinesplt) - 1:
                runs = 0
                break


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        run = True
        listenThread = threading.Thread(target=receive, args=(s,))
        listenThread.setDaemon(True)
        listenThread.start()
        while run:
            s.send(input().encode("utf8"))
