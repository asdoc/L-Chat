from sys import argv
from Tkinter import Frame, Tk, Frame, BOTH, Entry, Button, RIGHT, StringVar
from ttk import Label, Scale, Style
from chat_lib import Communication
import threading

class thread_recv_msg(threading.Thread):
	def __init__(self,my_port):
		threading.Thread.__init__(self)
		self.my_port = my_port
	def run(self):
		while True:
			msg,address = my_communication.recv()
			app.msg_recieved(address+": "+msg)
		
class Connection:
	ip=''
	my_port = 0
	send_port = 0
	def send_msg(self,msg):
		my_communication.send(msg)
	def recv_msg(self):
		thread_recv = thread_recv_msg(self.my_port)
		thread_recv.start()		

class Ui(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent, background="white")   
		self.parent = parent
		self.initUI()

	def initUI(self):
		self.parent.title("Simple")
		self.pack(fill=BOTH, expand=1)
		self.label_string = StringVar()
		self.label = Label(self, text=0, textvariable=self.label_string)        
		self.label.place(x=20, y=20)
		self.e = Entry(self)
		self.e.pack()
		self.button = Button(self, text="OK", command = self.send_msg)
		self.button.pack(side=RIGHT)
		my_connection.recv_msg()
	
	def send_msg(self):
		my_connection.send_msg(self.e.get())
		
	def msg_recieved(self,msg):
		self.label_string.set(msg)
		

my_connection = Connection()
if len(argv)!=4:
	print "Usage: python app.py <ip> <port to listen> <port to send>"
	exit(0)
my_connection.ip = argv[1]
my_connection.my_port = int(argv[2])
my_connection.send_port = int(argv[3])
my_communication = Communication(my_connection.ip,my_connection.my_port,my_connection.send_port)
        
root = Tk()
root.geometry("250x150+300+300")
app = Ui(root)
root.mainloop()
