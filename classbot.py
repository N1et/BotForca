# encoding: UTF-8
from time import sleep
class ircbot(object):
	def __init__(self, socket):
		self.socket = socket
		self.listch = []
	def set_cred(self, nick, username="bot", realname="bot"):
		socket = self.socket
		cmd = [("USER %s %s %s :%s\n" %(username, username, username, realname) ), ("NICK %s\n" %nick)]
		socket.send(cmd[0])
		sleep(2)
		socket.send(cmd[1])
		sleep(2)
		self.nick = nick

	def change_nick(self, nick):
		socket = self.socket
		cmd = "NICK %s\n" %nickmpkpk.hukfj
		socket.send(cmd)
		sleep(1)

	def join(self, channel):
		socket = self.socket
		self.listch
		if not( channel.startswith("#") ):
			channel = "#"+channel
		cmd = ("JOIN %s\n" %channel)
		socket.send(cmd)
		self.listch.append(channel)
		sleep(2)

	def unjoin(self, channel):
		socket = self.socket
		listch = self.listch
		if not(channel.startswith("#") ):
			channel = "#"+channel
		cmd = "PART %s\n" %channel
		socket.send(cmd)
		self.listch.remove(channel)
		sleep(2)
	def chlist(self):
		return self.listch
	def recv(self, size=1024):
		socket = self.socket
		data = socket.recv(1024)
		if data.find("PRIVMSG") == -1:
			return "",""
		try:
			data = data.split("!")
			nick = data[0].split(":")[1]
			msg = data[1].split(":")[1]
			return nick, msg
		except:
			return "",""

	def sendmsg(self, text, channel=None):
		if not channel:
			channel = self.listch[0]
		socket = self.socket
		cmd = ("PRIVMSG %s %s\n" %(channel, text))
		socket.send(cmd)
