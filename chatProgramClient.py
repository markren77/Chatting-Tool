# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 19:10:50 2021

@author: Mark
"""

import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
data = ""

while data!='exit':
    serverResponse = s.recv(1024).decode("utf-8")
    print("Server: " + serverResponse)
    data = input()
    s.send(data.encode())
    
s.close()

