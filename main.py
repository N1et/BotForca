from socket import *
import ssl
from classbot import *
from time import sleep
from forca import Forca
server = ""
port = 6697 # ssl
channelirc = "#lala"
sock = socket(AF_INET, SOCK_STREAM)
sock = ssl.wrap_socket(sock)
sock.connect((server, port))
ircbot = ircbot(sock)
ircbot.set_cred("mamacita")
while 1:
    data = sock.recv(1024)
    if data.find("PING") != -1:
        pong = data.split()[1]
        sock.send("PONG "+pong+"\n")
        print "Ping respondido!"
        sleep(2)
        break
ircbot.join(channelirc)
party = Forca("carro")
msg = party.re_word()
ircbot.sendmsg("%s %i Letras" %(party.re_word(), party.letter_len))
while 1:
    nick, msg = ircbot.recv(1024)
    if not (nick and msg):
        continue
    if party.word == party.str_adiv: #essa parte ta com erro, dps resolvo
        ircbot.sendmsg("Ninguem acertou")
        break
    if not party.letter(msg[0:-2]):
        ircbot.sendmsg(nick+": Nao possui essa letra")
        continue
    emword = party.re_word()
    ircbot.sendmsg(emword)


    
