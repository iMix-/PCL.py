# Stuff imported
import hashlib

# Crypt.py - Contains all crypt methods
class Crypt():
	def MD5(self, string):
		hashObj = hashlib.md5();
		string.encode('utf-8')
		hashObj.update(string.encode('utf-8'))
		return hashObj.hexdigest()
	
	def EncryptPassword(self, password):
		hashedPass = self.MD5(password)
		hashedPass = hashedPass[16:32] + hashedPass[0:16]
		return hashedPass
	
	def GetLoginHash(self, password, rndk):
		return self.EncryptPassword(self.EncryptPassword(password).upper() + rndk + "a1ebe00441f5aecb185d0ec178ca2305Y(02.>'H}t\":E1_root")
	
	def GetGameHash(self, lkey, rndk):
		return self.EncryptPassword(lkey + rndk) + lkey
