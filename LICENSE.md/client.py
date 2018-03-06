import time
from socket import *

Host = ''
Port = 1234
Bufsize = 1024

ADDR = (Host, Port)

tcpClient = socket( AF_INET, SOCK_STREAM )
tcpClient.connect( ADDR )

while True:
    data = raw_input('~:')
    if not data:
        break
    tcpClient.send(data)
    data = tcpClient.recv(Bufsize)
    if not data:
        break
    print data

tcpClient.close()
tcpServer.close()
