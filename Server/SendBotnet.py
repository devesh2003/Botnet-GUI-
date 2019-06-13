import socket
import pickle
import os

try:
    os.chdir("Server")
except:
    pass

class Send():
    def __init__(self,master_sock):
        self.master = master_sock
        self.read_botnet()
        botnetPkt = self.make_botnet_packet()
        self.master.send(botnetPkt)

    def make_botnet_packet(self):
        pkt = pickle.dumps(self.bots)
        return pkt

    def read_botnet(self):
        botnet = open("bots.txt","r")
        bots = botnet.read().split('\n')
        self.bots = bots
        botnet.close()

