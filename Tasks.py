# Stuff imported
import Socket
import User
import threading
from Xt import *

# Tasks.py - Has all task methods such as messages, moving, emotes, etc..
class Tasks:
	sock = None
	recv = None
	intRoomID = 2
	user = None
	
	def __init__(self, sock, user):
		self.sock = sock
		self.user = user
		self.BeginRecieve()
	
	def JoinRoom(self, roomID):
		self.sock.Send(CreateXt("j#jr", [str(roomID)], self.intRoomID))
	
	def SendPosition(self, x, y):
		self.sock.Send(CreateXt("u#sp", [str(x), str(y)], self.intRoomID))
	
	def SendEmote(self, emoteID):
		self.sock.Send(CreateXt("u#se", [emoteID], self.intRoomID))
		
	def SendSafeMessage(self, messageID):
		self.sock.Send(CreateXt("u#ss", [messageID], self.intRoomID))
	
	# This will be updated to pcam in later versions
	def SendMessage(self, message):
		self.sock.Send(CreateXt("m#sm", [self.user.ID, message], self.intRoomID))
	
	def SendFrame(self, frame):
		self.sock.Send(CreateXt("u#sf", [frame], self.intRoomID))
	
	def ThrowBall(self, x, y):
		self.sock.Send(CreateXt("u#sb", [x, y], self.intRoomID))
	
	def AddStamp(self, stamp):
		self.sock.Send(CreateXt("st#sse", [stamp], self.intRoomID))
	
	def AddItem(self, itemID):
		self.sock.Send(CreateXt("i#ai", [itemID], self.intRoomID))
		
	def AddFurniture(self, furnID):
		self.sock.Send(CreateXt("i#af", [furnID], self.intRoomID))
	
	def BeginRecieve(self):
		thread = threading.Thread(target = self.ContiniousRecv)
		thread.start()
		
	def ContiniousRecv(self):
		while True:
			try:
				recv = self.sock.Recv()
				if recv != None:
					self.recv = recv
					self.intRoomID = int(self.recv.split('%')[3])
			except ValueError:
				pass
