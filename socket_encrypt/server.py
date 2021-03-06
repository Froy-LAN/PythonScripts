#!/usr/bin/env python3
#it is necessary to install the cryptgraphy library using 'pip install cryptography'

import socket
from cryptography.fernet import Fernet

message = "You are connected to the server"

encryption_key = Fernet.generate_key()   #generate encryption key
fernet = Fernet(encryption_key)          

encrypted_message = fernet.encrypt(message.encode())  #encrypt message

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 7777)) #the consecutive single quotes ('') can be replaced be socket.gethostname() if both files are tested on the same host
s.listen()

while True:
	clientsocket, IP = s.accept()                         #accept connection from client
	print("Client with IP address {} has connected ".format(IP[0]))   #print IP address of connecting client
	clientsocket.send(encrypted_message)                   #send message
