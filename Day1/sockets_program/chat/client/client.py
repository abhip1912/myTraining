import socket
import threading
import time
s = socket.socket()
s.connect((socket.gethostname(), 1234))


def send():
    while True:
        ip = input()
        if len(ip) != 0:
            s.send(("\t\t\t\t" + ip).encode())


def receive():
    while True:
        print(s.recv(64).decode()+"  "+time.ctime().split()[3][:5])


thread1 = threading.Thread(target=receive)
thread2 = threading.Thread(target=send)
thread1.start()
thread2.start()
