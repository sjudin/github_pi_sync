import socket

SERVER_IP = '192.168.0.102'

s = socket.socket()
host = socket.gethostname()
PORT_NUMBER = 1500

s.connect((SERVER_IP, PORT_NUMBER))

print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

s.send('This is a message')
