__author__ = 'oun1982'
from socket import *
from time import ctime

HOST = 'localhost'
PORT = 5000
BUFFER_SIZE = 1024
ADDRESS = (HOST,PORT)

server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

while True:
    print('waiting for connection...')
    client, address = server.accept()
    print('Connection from : ',address)
    data_byte = str.encode(ctime())
    client.send(data_byte)
    client.close()

