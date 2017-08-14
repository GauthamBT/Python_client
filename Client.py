import socket
from _socket import SOCK_STREAM, AF_INET
import os

clientSocket = socket.socket(AF_INET, SOCK_STREAM, 0)

clientSocket.connect(("127.0.0.1", 8888))

buffer = clientSocket.recv(1024).decode("utf-8")

print("Buffer: ", buffer)

clientSocket.send(b'Thanks server')

buffer = None

while c != None:
    c = clientSocket.recv(1)
    buffer = buffer + c



file = open("client_new.txt", "wb+")

file.write(buffer)

file.close()

clientSocket.close()