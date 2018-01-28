__author__ = 'oun1982'
from socket import *

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024
ADDRESS = (HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.connect(ADDRESS)
data_byte = server.recv(BUFFER_SIZE)
dayAndTime = bytes.decode(data_byte)
print(dayAndTime)
server.close()
