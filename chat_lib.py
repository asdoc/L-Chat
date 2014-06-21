import socket

class Communication:

	def __init__(self,ip,my_port,send_port):
		self.ip = ip
		self.my_port = my_port
		self.send_port = send_port
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.bind(('', self.my_port))
		
	def recv(self):
		self.serversocket.listen(5)
		while True:
			connection, address = self.serversocket.accept()
			buf = connection.recv(64)
			if len(buf)> 0:
				return buf
				break
		return None
	
	def send(self,msg):
		clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		clientsocket.connect((self.ip, self.send_port))
		clientsocket.send(msg)

