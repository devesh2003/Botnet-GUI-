from tkinter import *
import Refresh
import socket

class CommandAndControl():
    def __init__(self,ip="127.0.0.1",port=2001,geometry="500x300"):
        self.ip = ip
        self.port = port

        self.root = Tk()
        self.root.iconbitmap('icon.ico')
        self.root.title("Bolt Botnet")
        self.root.geometry(geometry)

        self.create_labels()
        self.create_commandInput()
        self.create_exexButton()
        self.create_refreshButton()
        self.start()

    def refresh_Botnet(self):
        try:
            #Creates a socket for a Refresh request
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.ip,self.port-1))
            refresh = Refresh.Refresh(s)
            refresh.refresh()
            botnet = refresh.getBots()
            self.bot_list.delete('0','end')
            index = 1
            # print(type(botnet))
            for bot in botnet:
                # print(type(bot))
                self.bot_list.insert(index,bot)
                index += 1
        except Exception as e:
            print("[*]Error in refresh_Botnet : %s"%(str(e)))

    def create_refreshButton(self):
        #Creates new frame
        but_frame = Frame(self.root)
        but_frame.place(x=180,y=45)

        refresh_Button = Button(but_frame,text="Refresh",width=15,command=self.refresh_Botnet)
        refresh_Button.pack()

    def process_cmd(self):
        cmd = self.get_command()
        pass


    def create_exexButton(self):
        #Creates new Frame
        button_frame = Frame(self.root)
        button_frame.place(x=175,y=260)

        #Creates Button
        exec_button = Button(button_frame,text="Execute",width=15,command=self.process_cmd)
        exec_button.pack()

    def get_command(self):
        return self.cmd.get()

    def create_commandInput(self):
        #Creates new Frame
        sym = Frame(self.root)
        sym.place(x=83,y=217)

        #Creates '>' Symbol
        symb = Label(sym,text='>',font=('Arial',25))
        symb.pack()

        #Creates new Frame
        cmd_frame = Frame(self.root)
        cmd_frame.place(x=110,y=230)

        #Creates input field for Commands
        cmd_input = Entry(cmd_frame,width=41)
        cmd_input.grid()
        self.cmd = cmd_input

    def create_labels(self):
        #Creates the Title Frame and Label
        title_frame = Frame(self.root)
        title_frame.place(x=250,y=20,anchor="center")
        title = Label(title_frame,text="Command And Control Center",font=("Bold",'20'))
        title.pack()

        #Creates new Frame
        bots_disp_frame = Frame(self.root)
        bots_disp_frame.place(x=110,y=85)

        #Creates scrollbar
        scroll_bots = Scrollbar(bots_disp_frame)
        scroll_bots.pack(side=RIGHT,fill=Y)
        
        #Creates a container of Active Bots on the Bolt Network
        bot_list = Listbox(bots_disp_frame,width=40,height=8,
                            yscrollcommand=scroll_bots.set)
        bot_list.pack(side=LEFT)

        #Sets the list to go down with change in ordinate
        scroll_bots.config(command=bot_list.yview)
        self.bot_list = bot_list

    def start(self):
        self.root.mainloop()

    def stop(self):
        self.root.destroy()