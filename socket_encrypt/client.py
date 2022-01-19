#!/usr/bin/env python3
#It is assumed both client and server scripts will run on the same host

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 7777)) #replace 'socket.gethostname()' with IP address of host that functions as server.
                                        
msg = s.recv(1024)
print(msg)
