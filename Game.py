# Stuff imported
import Socket
import Crypt
import User
import ServerList

# Game.py - Defines all world authentication methods
class Game:
	user = None
	Sock = None
	
	def __init__(self, user, server):
		self.user = user
		ServerDeats = ServerList.GetServerDetails(server)
		self.Sock = Socket.SocketClient(ServerDeats.split(':')[0], int(ServerDeats.split(':')[1]))
		self.Sock.Connect()
		self.Authenticate()
		
	def Authenticate(self):
		rndK = self.SendHandshake()
		self.SendLogin(rndK)
		
	# Returns string random key
	def SendHandshake(self):
		self.Sock.Send("<policy-file-request/>")
		self.Sock.Send("<msg t='sys'><body action='verChk' r='0'><ver v='153' /></body></msg>")
		rndKPacket = self.Sock.Send("<msg t='sys'><body action='rndK' r='-1'></body></msg>")
		rndK = self.stribet(rndKPacket, "<k>", "</k>")
		print("[Grabbed rndK]: " + rndK)
		return rndK
	
	def SendLogin(self, rndK):
		c = Crypt.Crypt()
		recv = self.Sock.Send("<msg t='sys'><body action='login' r='0'><login z='w1'><nick><![CDATA[" + str(self.user.Userstring) + "]]></nick><pword><![CDATA[" + c.GetGameHash(str(self.user.LoginKey), rndK) + '#' + str(self.user.ConfirmationHash) + "]]></pword></login></body></msg>")
		self.Sock.Send("%xt%s%j#js%-1%" + str(self.user.ID) + "%" + self.user.LoginKey + "%en%")

	# Thanks 'cji' on stack overflow, I was too lazy to make my own version of this
	def stribet(self, s, first, last):
		start = s.index( first ) + len( first )
		end = s.index( last, start )
		return s[start:end]
