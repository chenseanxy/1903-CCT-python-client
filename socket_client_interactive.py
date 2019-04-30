import socket
import os


while True:
    line = input()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 30614))
    s.send(bytes(line, "utf-8"))
    s.close()
