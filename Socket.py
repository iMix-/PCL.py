# Stuff imported
import socket;

# Socket.py - used for managing socket stuff throughout the PCL
class SocketClient():
	ip = None
	port = None
	sock = None
	
	def __init__(self, ip, port):
		self.ip = ip
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
	def Connect(self):
		self.sock.connect((self.ip, self.port))
		print("Connection to " + self.ip + ":" + str(self.port) + " has succeeded")
	
	def Send(self, data):
		self.sock.send(bytes(data + "\0", "UTF-8"))
		print("[SEND]: " + data)
		return self.Recv()
		
	def Recv(self):
		recv = self.sock.recv(2048)
		if(recv != None):
			# This is freaking stupid, but idk what to do about it, really
			recvStr = recv.decode('utf-8')
			print("[RECV]: " + recvStr)
			return recvStr
		return None
