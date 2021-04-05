# server2.py
import socket
from threading import Thread
import threading
# from SocketServer import ThreadingMixIn // python2
from socketserver import ThreadingMixIn
import pickle
import os
TCP_IP = '0.0.0.0'
TCP_PORT = 9001
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock,n):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        self.n = n
        self.done = False
        print (" New thread started for "+ip+":"+str(port)+" " + str(n))

    def run(self):

        msg = self.sock.recv(BUFFER_SIZE)
        rsize = 0
        fsize =  int(msg.decode("ascii").strip())
        print("fsize: " + str(fsize))

        b=0
        filen = 'receivedc_' + str(self.n)
        with open(filen, 'wb') as f:
            print ('file opened')
            while rsize < fsize:
                b+=1
                data = self.sock.recv(BUFFER_SIZE)
                # print('data=%s', (data) )
                print('rsize' + str(rsize))
                
                if not data or data == 'END':
                    self.sock.close()
                    print ('file close()')

                    break
                elif rsize >= fsize:
                    f.close()
                    break                    
                else:                    
                    f.write(data)
                    print("writing " + str(b))
                    rsize = rsize + len(data)
                    print("------------")
        f.close()
        print('Successfully received file from client: ' + str(self.n))

        # a = a+1
        filename='server_model.pt'
        f = open(filename,'rb')
        while True:
            print("sending")
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break
            print('Successfully sent file to client: ' + str(self.n))

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []
threadLock = threading.Lock()
a = 0 

while True:
    tcpsock.listen(5)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn,a)
    newthread.start()
    threads.append(newthread)
    a=a+1

for t in threads:
    t.join()


