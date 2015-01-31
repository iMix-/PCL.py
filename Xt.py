def CreateXt(prefix, args, intRoomID):
	packet = "%xt%s%"
	packet += str(prefix) + '%';
	packet += str(intRoomID) + '%'
	for arg in args:
		packet += str(arg) + '%'
	return packet

