# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:04:17 2021

@author: Mark
"""

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 1234))
s.listen(5)
clientsocket, address = s.accept()
print(f"Connection from {address} has been established.")
clientsocket.send("You are now connected to the chat server, say hi!\n".encode())
while True:
    clientMessage = clientsocket.recv(1024).decode("utf-8")    
    if clientMessage=="exit":
        break
    print("Client: " + clientMessage)
    serverMessage = input()
    clientsocket.send(serverMessage.encode())

print("The client has disconnected, closing server...")
clientsocket.close()
    
