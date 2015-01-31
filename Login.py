# Stuff imported
import Socket
import Crypt
import User

# Login.py - Defines all login methods
class Login():
	user = None
	Sock = None
	
	def __init__(self, Username, Password):
		self.user = User.User()
		self.user.Username = Username
		self.user.Password = Password
		self.Sock = Socket.SocketClient("204.75.167.165", 3724)
		self.Sock.Connect()
		self.StartLogin()
	
	def StartLogin(self):
		rndK = self.SendHandshake()
		u = self.SendLoginPacket(rndK)
		return u
		
	# Returns string random key
	def SendHandshake(self):
		self.Sock.Send("<policy-file-request/>")
		self.Sock.Send("<msg t='sys'><body action='verChk' r='0'><ver v='153' /></body></msg>")
		rndKPacket = self.Sock.Send("<msg t='sys'><body action='rndK' r='-1'></body></msg>")
		rndK = self.stribet(rndKPacket, "<k>", "</k>")
		print("[Grabbed rndK]: " + rndK)
		return rndK
	
	def SendLoginPacket(self, rndK):
		c = Crypt.Crypt()
		recv = self.Sock.Send("<msg t='sys'><body action='login' r='0'><login z='w1'><nick><![CDATA[" + self.user.Username + "]]></nick><pword><![CDATA[" + c.GetLoginHash(self.user.Password, rndK) + "]]></pword></login></body></msg>")
		packetElements = recv.split('%')
		userData = packetElements[4].split('|')
		self.user.ID = userData[0]
		self.user.Userstring = packetElements[4]
		self.user.ConfirmationHash = packetElements[5]
		self.user.FriendsKey = packetElements[6]
		self.user.SWID = userData[1]
		self.user.LoginKey = userData[3]
	
	def GetUser(self):
		return self.user
	
	# Thanks 'cji' on stack overflow, I was too lazy to make my own version of this
	def stribet(self, s, first, last):
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
