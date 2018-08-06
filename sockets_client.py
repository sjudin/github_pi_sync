import socket
import datetime

SERVER_IP = '192.168.0.102'

s = socket.socket()
host = socket.gethostname()
PORT_NUMBER = 1500

s.connect((SERVER_IP, PORT_NUMBER))

print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

print(s.recv(1024))

s.send(str(datetime.datetime.now()).encode('UTF-8'))
s.close()
