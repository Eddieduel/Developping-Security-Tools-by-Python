import time
from socket import *

Host = ''
Port = 1234
Bufsize = 1024

ADDR = (Host,Port)

tcpServer = socket(AF_INET,SOCK_STREAM)
tcpServer.bind(ADDR)
tcpServer.listen(5)

while True:
    print 'waitting for connection'
    tcpClient,addr = tcpServer.accept()
    print 'connect from:'addr
    while True:
        data = tcpClient(Bufsize)
        if not data:
            break
        tcpClient.send('%s %s'%(time.ctime(),data))
        
tcpClient.close()
tcpServer.close()


'''
#反弹shell
from subprocess import PIPE,Popen

cmd = Propen(['/bin/bash','-c',data],stdin=PIPE,stdout=PIPE)

#ping

ping = Propen(['/bin/bash','-c',ping -c,data],stdin=PIPE,stdout=PIPE)
data = ping.stout.read()
'''
