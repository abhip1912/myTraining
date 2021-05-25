import socket

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((socket.gethostname(), 5695))
# become a server socket
serversocket.listen(5)
print("Running the server...")

while True:
    (clientsocket, address) = serversocket.accept()
    print(f"ClientSocket connected : {clientsocket} & Address : {address}")
    clientsocket.send(("Thank you for connecting...").encode())
    dataSize = int(clientsocket.recv(512).decode())
    print(f"DataSize is : {dataSize} & it's type is: {type(dataSize)}")
    data = clientsocket.recv(dataSize).decode()
    print(data)
