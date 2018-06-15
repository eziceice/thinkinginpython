import socket

s = socket.socket()
s.connect((socket.gethostname(), 1234))
print(s.recv(1024))