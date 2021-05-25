import socket
import threading
import time
s = socket.socket()
s.bind((socket.gethostname(), 1234))
print("Socket is binded at 1234 port.")

s.listen()
print("Socket is listening...")


def send(clientSocket, addr):
    while True:
        ip = input()
        if len(ip) != 0:
            clientSocket.send(("\t\t\t\t"+ip).encode())


def receive(clientSocket, addr):
    while clientSocket is not None:
        ip = clientSocket.recv(64).decode()
        print(ip+"  "+time.ctime().split()[3][:5])


while True:
    clientSocket, addr = s.accept()
    thread1 = threading.Thread(target=receive, args=(clientSocket, addr))
    thread2 = threading.Thread(target=send, args=(clientSocket, addr))
    thread1.start()
    thread2.start()
