import socket
from sys import getsizeof

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("Abhi-Laptop", 5695))
print(s.recv(512).decode())
MSG = "This is sending from client.py file...".encode()
s.send(str(getsizeof(MSG)).encode())
s.send(MSG)
