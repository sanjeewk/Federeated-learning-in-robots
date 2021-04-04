
# client2.py
#!/usr/bin/env python

import socket
import time 
TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

filename='best.pt'
f = open(filename,'rb')
while True:   
    l = f.read(BUFFER_SIZE)
    while (l):
        self.sock.send(l)
        #print('Sent ',repr(l))
        l = f.read(BUFFER_SIZE)
    if not l:
        f.close()
        self.sock.close()
        break
print('Successfully sent the file to server')

with open('best.pt', 'wb') as f:
    print ('file opened')
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        # print('data=%s', (data))
        if not data:
            f.close()
            print ('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully recived the file from server')
s.close()
print('connection closed')
