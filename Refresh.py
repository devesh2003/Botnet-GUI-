import socket
import pickle
import InitPacket

class Refresh():
    def __init__(self,server_sock):
        self.serv = server_sock
    
    def refresh(self):
        #Send the Init Packet
        arch = InitPacket.create("refresh")
        pkt = arch.make()
        self.serv.send(pkt)
        raw_botnet = self.serv.recv(4096)
        botnet = pickle.loads(raw_botnet)
        self.bots = botnet
        self.serv.close() 

    def getBots(self):
        return self.bots
