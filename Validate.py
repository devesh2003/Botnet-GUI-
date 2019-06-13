import socket
import struct
from time import sleep

class validate():
    def __init__(self,username,password,ip,port=2000):
        self.username = username
        self.password = password
        self.ip = ip
        self.port = port
        self.test_server()
        self.validate()

    def test_server(self):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((self.ip,int(self.port+1)))
            self.status = True
            s.close()
        except socket.error:
            self.status = False

    def make_validatePkt(self):
        validatePkt = struct.pack("<HH1s",21,2003,"V".encode())
        return validatePkt 
        
    def validate(self):
        if self.status:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.ip,self.port))

            #Sets the connection global
            self.conn = s

            s.send(self.make_validatePkt())
            sleep(1)
            data_packet = struct.pack("<HH%ds%ds"%(len(self.username),len(self.password)),len(self.username),
                                                len(self.password),self.username.encode(),self.password.encode())
            s.send(data_packet)
            resp = s.recv(1024).decode()
            if resp == "A":
                self.valid = True
            else:
                self.valid = False
        else:
            self.valid = False
            
    def check(self):
        return self.valid
