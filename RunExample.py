import Login
import Game
import User
import Tasks
import time

# Login to those credidentals
login = Login.Login("Username", "password")
# Get user object to pass it to game object constructor
user = login.GetUser()
# Create game object and log on server "Permafrost"
game = Game.Game(user, "Permafrost")
# Get SocketClient object from game object to pass it on to the Tasks object
sock = game.Sock
# Create tasks object
tasks = Tasks.Tasks(sock, user)
# Join room ID 100 (Town)
tasks.JoinRoom(100)
while True:
	# Keep sending emote ID 1 (:D) every 4 seconds
	tasks.SendEmote(1)
	time.sleep(4)
