import socket
import time


s = socket.socket()

host = socket.gethostname()
port = 1500
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting!')
    c.close()
    time.sleep(1)
    