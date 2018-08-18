import socket

from datetime import datetime


def make_unicode(input):
    if type(input) is str:
        return input.encode('utf-8')
    else:
        return input.decode('utf-8')


s = socket.socket()

host = socket.gethostname()
port = 1500
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send(make_unicode('Thank you for connecting!'))

    recv = make_unicode(c.recv(1024))

    if recv is '1':
        c.send(make_unicode(str(datetime.now())))
        print('Sent time!')

    elif recv is '2':
        c.send(make_unicode('test'))
        print('Sent test')

    c.close()
