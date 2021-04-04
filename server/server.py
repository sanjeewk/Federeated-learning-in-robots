# server2.py
import socket
from threading import Thread
# from SocketServer import ThreadingMixIn // python2
from socketserver import ThreadingMixIn

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock,n):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        self.n = n 
        print (" New thread started for "+ip+":"+str(port))

    def run(self):
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

        print('Successfully received file from client: ' + str(self.n))

        a = a+1
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
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()


