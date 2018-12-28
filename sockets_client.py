import socket


def make_unicode(input):
    if type(input) is str:
        return input.encode('utf-8')
    else:
        return input.decode('utf-8')


SERVER_IP = '192.168.0.100'

s = socket.socket()
host = socket.gethostname()
PORT_NUMBER = 1500

s.connect((SERVER_IP, PORT_NUMBER))

print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

print(make_unicode(s.recv(1024)))

i = input('Enter your input\n')

s.send(make_unicode(i))
print(make_unicode(s.recv(1024)))

s.close()

