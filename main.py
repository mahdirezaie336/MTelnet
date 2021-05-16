import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('smtp.google.com', 25))
print(s.recv(4096).decode())
