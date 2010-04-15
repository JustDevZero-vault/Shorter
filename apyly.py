#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen
from exceptions import IndexError, IOError
from sys import argv
#       pyly.py written in python2.8
#       version 1.4
#       Copyright 2010 Mephiston <meph.snake@gmail.com>
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3.0 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, get a copy on http://www.gnu.org/licenses/gpl.txt

#------------------------------ Utilities --------------------------------------- #
# The main purpose of this script is to easily give urls with bit.ly service.
# It shorts the url anonymously.
#--------------------------- CHANGE LOG ----------------------------------------- #
#       1.0     Initial release
#       1.1     Improved the speed (only a little), deleted some splitting process
#       1.2     Added a system argument function, you can choose between the sys.argv or ask function.
#               By changing the line 75 for sysRun() or askRun()
#       1.3     Fixed bugs, errors are treated as exceptions.
#       1.4     Some prints become "returns", because it allows to use it externally
#--------------------------- TESTED IN ------------------------------------------ #
#       GNU/Linux (all distros)     WINDOWS NT*         MacOSX      *BSD

def splitter(responde):
    try:
        opened=responde.split('var SHORTEN_RESULT = {') [1]
        closed=opened.split('};') [0]
        cleaned=closed.split('"')
        #Here we make a splitting process, for cleaning data, and giving the url.
        return cleaned[17]
    except IndexError:
        return 'The URL was not recognized.'
        #If the url is not recognized, it causes an exception.


def shorten_url(url):
    try:
        longUrl = (url)
        encodeurl='http://bit.ly/%s' % (longUrl)
        request = urlopen(encodeurl)
        responde = request.read ()
        request.close()
        return splitter(responde)
        #Resquesting the for the url, and doing the split.
    except IOError, e:
        raise 'Ops! An I/O error happened.'
        #Obviously, is obvious.

def sysRun():
    #If you chose sysRun, it will use the url provided in your command line.
    try:
        return shorten_url(argv[1])
    except IndexError:
        return 'The URL was not provided.'

def askRun():
    url=str(raw_input('Insert the url that you want to shorten: '))
    if url!='':
        return shorten_url(url)
    else:
        return 'The URL was not provided.'


try:
    if __name__ == '__main__':
        print sysRun()
except KeyboardInterrupt:
    print '\nThe progam was interrupted.'