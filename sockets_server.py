import socket

from datetime import datetime

s = socket.socket()

host = socket.gethostname()
port = 1500
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting!'.encode('UTF-8'))

    recv = c.recv(1024).decode('utf-8')

    if recv is 'time':
        c.send(str(datetime.now()).encode('utf-8'))

    c.close()
