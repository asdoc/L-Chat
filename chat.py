from chat_lib import Communication
from sys import argv
import threading

class thread_recv_msg(threading.Thread):
	def __init__(self,my_port):
		threading.Thread.__init__(self)
		self.my_port = my_port
		self.my_communication = Communication(None,9491,None)
	def run(self):
		while True:
			msg_packet = self.my_communication.recv()
			''' send the recieved packet to the main_loop_obj '''
			main_loop_obj.msg_recieved(msg_packet)

class group_chat():
	def __init__(self,group_id):
		if group_id == None:
			# TODO generate self.group_id
			pass
			
		else:
			self.group_id = group_id
		# TODO create UI
		pass
		
	def add( tupple_ip ):
		# TODO send "GRP ADD self.group_id" to all IPs in tupple_ip
		pass
		
	def send(self,msg):
		# TODO send "MSG self.group_id ___" to self.ip
		pass

class private_chat():
	def __init__(self,ip):
		self.ip = ip
		# TODO create UI
		pass
		
	def send(self,msg):
		# TODO send "MSG PVT ___" to self.ip
		pass

class public_chat():
	def __init__(self):
		# TODO create UI
		pass
		
	def send(self,msg):
		# TODO send "MSG PUB ___" to all IPs in main_loop_obj.online_dict
		pass

class main_loop():
	''' A dict for storing {'ip': 'name' }'''
	online_dict = {}
	
	def __init__(self,name):
		# TODO create UI
	
		''' Start the thread for recieving messages '''
		thread_recv_msg(9491).start()
		
		# TODO send "RESPOND NAME" to all IP ports on network

	def msg_recieved(self,msg_packet):
		# TODO implement all message recieved protocols
		pass


if __name__ == '__main__':
	name = argv[1]
	main_loop_obj = main_loop(name)
