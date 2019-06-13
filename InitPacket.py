import struct

class create():
    def __init__(self,pkt_type):
        self.type = pkt_type
    
    def make(self):
        if self.type.upper() == "REFRESH":
            return struct.pack("<HH1s",21,1,"R".encode())
        elif self.type.upper() == "VALIDATE":
            return struct.pack("<HH1s",21,1,"V".encode())
        elif self.type.upper() == "EXECUTE":
            return struct.pack("<HH1s",21,1,"E".encode())