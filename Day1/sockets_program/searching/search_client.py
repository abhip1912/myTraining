import socket
import threading

s = socket.socket()
s.connect((socket.gethostname(), 55555))
s.send(str(([19, 21, 13, 74, 15], 19)).encode())
print(s.recv(512).decode())
s.send(str(([19, 21, 13, 74, 15], 2)).encode())
print(s.recv(512).decode())
