from tkinter import *
import Validate 

#Original : 280x100

class HomePage(): 
    def __init__(self,title="Bolt Botnet",geometry="280x150"):
        self.status = False
        self.root = Tk()
        self.root.iconbitmap('icon.ico')
       # self.root.call('wm', 'iconphoto', self.root._w, PhotoImage(file='icon.gif'))
        self.root.title(title)
        self.geometry = geometry
        self.set_size()
        self.create_fields()
        self.create_buttons()
        
    def set_size(self):
        self.root.geometry(self.geometry)

    def toggle_invalid(self):
        #Creates a new Frame for error message
        err = Frame(self.root)
        err.place(x=100,y=127)

        #Creates Error Label
        msg = Label(err,text="Access Denied!",font=("arial",10))
        msg.pack()

    def take_input(self):
        ip = self.ip.get()
        print(ip)
        username = self.username.get()
        password = self.password.get()
        process = Validate.validate(username,password,ip)
        result = process.check()
        if result:
            print("[*]Access Granted")
            self.status = True
            self.destroy()
        else:
            self.status = False
            self.toggle_invalid()
            print("[*]Access Denied")

    def create_buttons(self):
        login_frame = Frame(self.root)
        login_frame.place(x=125,y=100)
        login_button = Button(login_frame,text="Login",command=self.take_input)
        login_button.pack()

    def create_fields(self):
        #Creates Username Label and Entry Field
        user_frame = Frame(self.root)
        user_frame.place(x=125,y=25,anchor="center")
        user_label = Label(user_frame,text="Username : ")
        user_label.grid(row=1,column=1)
        
        user_entry = Entry(user_frame)
        user_entry.grid(row=1,column=2)
        self.username = user_entry

        #Creates Password Label and Entry Field
        pass_frame = Frame(self.root)
        pass_frame.place(x=125,y=50,anchor="center")
        pass_label = Label(pass_frame,text="Password : ")
        pass_label.grid(row=1,column=1)

        pass_entry = Entry(pass_frame)
        pass_entry.grid(row=1,column=2)
        self.password = pass_entry

        #Creates IP input Frame
        ip_frame = Frame(self.root)
        ip_frame.place(x=145,y=75,anchor="center")
        ip_label = Label(ip_frame,text="IP :")
        ip_label.grid(row=1,column=1)

        ip_entry = Entry(ip_frame)
        ip_entry.grid(row=1,column=2)
        self.ip = ip_entry

    def start(self):
        self.root.mainloop()

    def destroy(self):
        self.root.destroy()
