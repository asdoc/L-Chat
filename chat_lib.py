import socket

def recv(port):
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('', port))
	serversocket.listen(5)          #become a server socket, maximum 5 connections
	while True:
		connection, address = serversocket.accept()
		buf = connection.recv(64)
		if len(buf)> 0:
			return buf
			break
	return None
	
def send(ip,port,msg):
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.connect((ip, port))
	clientsocket.send(msg)

