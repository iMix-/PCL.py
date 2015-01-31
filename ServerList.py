# Stuff imported
import json
import io

def GetServerDetails(server):
	data = None
	with open ("Servers.json", "r") as jsonfile:
		data = jsonfile.read().replace('\n', '')
		j = json.loads(data)
		return j[server]["IP"] + ':' + str(j[server]["Port"])
