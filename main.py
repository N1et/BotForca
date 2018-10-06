from socket import *
import ssl
from classbot import *
from time import sleep
from forca import Forca
import sys
import random

try:
    server = sys.argv[1]
    port = int(sys.argv[2])
    channelirc = sys.argv[3]
    wordgame = sys.argv[4]
except:
    print "Example: "+sys.argv[0]+" irc.server.org 6667 canaldentario abelha"
    sys.exit()

sock = socket(AF_INET, SOCK_STREAM)
sock = ssl.wrap_socket(sock) #ssl
sock.connect((server, port))
ircbot = ircbot(sock)
ircbot.set_cred("mamacita")
while 1:
    data = sock.recv(1024)
    if data.find("PING") != -1:
        ircbot.pong(data)
        print "Ping respondido!"
        sleep(2)
        break
ircbot.join(channelirc)
party = Forca(wordgame)
msg = party.re_word()
ircbot.sendmsg("ch: LETRA")
ircbot.sendmsg("word: PALAVRA")
ircbot.sendmsg("%s %i Letras" %(party.re_word(), party.letter_len))
while 1:
    nick, msg = ircbot.recv(1024)
    if not (nick and msg):
        continue
    if msg.startswith("ch:"):
        msg = msg.split(":", 1)[1].replace(" ", "").lower()
        msg = msg[0:-2]
        if not party.letter(msg):
                #ircbot.sendmsg(nick+": Nao possui essa letra")
                choiceslist = ["voce ta vendo essa letra aqui ? palhaco", "uma porta eh mais inteligente que voce", "Animal!", ""]
                choice = random.choice(choiceslist)
                if choice != "":
                    ircbot.sendmsg(choice)

                pass
        else:
            fullword = party.re_word()
            ircbot.sendmsg(fullword)
    elif msg.startswith("word:"):
        msg = msg.split(":", 1)[1].replace(" ", "").lower()
        if not party.word_kick(msg):
            #ircbot.sendmsg(nick+": Essa Palavra nao existe")
            pass
        else:
            fullword = party.re_word()
            ircbot.sendmsg(fullword)

    
