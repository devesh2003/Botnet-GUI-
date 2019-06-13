import socket
import struct

class Handler():
    def __init__(self,bot_sock):
        self.conn = bot_sock
        pass

    def checkConn(self):
        pass