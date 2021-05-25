import socket
import threading

s = socket.socket()
s.bind((socket.gethostname(), 5555))


def task(c_obj, addr):

    while c_obj is not None:
        myList, value = eval(c_obj.recv(1024).decode())
        print(f"{addr} : {(myList, value)}")

        for i in range(len(myList)):
            if myList[i] == value:
                c_obj.send(f"{value} is at {i} index".encode())
                break
        else:
            c_obj.send(f"{value} is not present in the list !!".encode())
            break


s.listen()
print("Server is Running!!")
while True:
    c_obj, addr = s.accept()
    thread = threading.Thread(target=task, args=(c_obj, addr))
    thread.start()
