#!/usr/bin/env python
#*.*coding:utf-8*.*

#       pyly.py written in python2.6
#       version 1.0 (Alpha)
#       Copyright 2009 Mephiston <meph.snake@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2.1.1 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, get a copy on http://www.gnu.org/licenses/gpl.txt

#   ---------------- Generic utilities ---------------- #
#   A usefull an fun bot for irc. (For the moment is only fun)
#   -------------------- TODO LIST -------------------- *
#   Weather, define, lista, !say, query, a lot....

import sys
import socket
import string
import httplib
#import urllib
 
network = 'irc.freenode.com'
port = 6667
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
password='passwordforthebot'
irc.send ( 'NICK nickforthebot\r\n' )
irc.send ( 'USER nickforthebot nickforthebot nickforthebot :Python IRC\r\n' )
irc.send ( 'JOIN #hellteam\r\n' )
irc.send ( 'PRIVMSG #hellteam :Buenas a todos!!!!.\r\n' )
lista=['No me da la gana', '¿Para algo tienes Google no?', 'Que me dejes!', 'Me chivare a Mephiston', 'Que no, que no te pienso dar porno!']
n=0

# Private messages
while True:
    data = irc.recv ( 4096 )
    NOMBRE = str(data.split('!')[0])
    NOMBRE = str(NOMBRE.split(':')[1])
    if data.find ( '+iwR' ) !=-1:
        irc.send ( 'NS IDENTIFY '+ str(ppasword) + '\r\n' )
    if data.find ( 'PING' ) != -1:
        irc.send ( 'PONG ' + data.split() [ 1 ] + '\r\n' )
    elif data.find ( ':mephiston!n=daniel@unaffiliated/mephiston PRIVMSG #hellteam :!muere' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Esta bien, %s, si no me quieres...\r\n' % (NOMBRE))
        irc.send ( 'QUIT\r\n' )
    elif data.find ( '!hora' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Buenas %s :-D \r\n'  % (NOMBRE))
    elif data.find ( 'buenas' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Buenas %s :-D \r\n'  % (NOMBRE))
    elif data.find ( 'hola' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Buenas %s :-D \r\n'  % (NOMBRE))
    elif data.find ( 'nas' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Buenas %s :-D \r\n'  % (NOMBRE))
    elif data.find ( 'HOLA' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Buenas %s :-D \r\n'  % (NOMBRE))
    elif data.find ( 'culpa' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Choms, por supuesto \r\n' )
    elif data.find ( '!porno' ) != -1:
        if data.find ( '!porno' ) != -1:
            FRASE=lista[n]
            n+=1
        irc.send ( 'PRIVMSG #hellteam :%s \r\n'  % (FRASE))
    elif data.find ( 'KICK' ) != -1:
        irc.send ( 'JOIN #hellteam\r\n' )
    elif data.find ( '!operame' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Lo siento %s aun esta funcion no ha sido implementada \r\n' % (NOMBRE))
    elif data.find ( 'piedra' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :Le informo, %s, que la constitucion de hellteam protege severamente a las piedras.\r\n' % (NOMBRE))
    elif data.find ( '!rodadora' ) != -1:
        irc.send ( 'PRIVMSG #hellteam :......@ \r\n' )
        irc.send ( 'PRIVMSG #hellteam :............@ \r\n' )
        irc.send ( 'PRIVMSG #hellteam :..................@ \r\n' )
        irc.send ( 'PRIVMSG #hellteam :........................@ \r\n' )
    print data
