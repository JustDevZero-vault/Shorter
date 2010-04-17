#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen, urlencode
from exceptions import IndexError, IOError
from sys import argv
from re import match
#       isgd.py written in python2.8
#       version 1.0
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
# The main purpose of this script is to easily give urls with is.gd service.
# It shorts the url anonymously.
#--------------------------- CHANGE LOG ----------------------------------------- #
#       1.0     Initial release
#--------------------------- TESTED IN ------------------------------------------ #
#       GNU/Linux (all distros)     WINDOWS NT*         MacOSX      *BSD



def check_url(long_url):
    if match("^https?://[^ ]+|^ftp?://[^ ]+|^sftp?://[^ ]+", long_url):
        return True
    else:
        return False

def shorten_url(long_url):
    if check_url(long_url):
        try:
            longUrl=urlencode(dict(longurl=long_url))
            encodeurl='http://is.gd/api.php?%s' % (longUrl)
            request = urlopen(encodeurl)
            responde = request.read ()
            request.close()
            return responde
            #Resquesting for the url
        except IOError, e:
            return 'Error: An I/O error happened.'
        #Obviously, is obvious.
    else:
        return "Error: The URL was not provided."

def sysRun():
    #If you chose sysRun, it will use the url provided in your command line.
    try:
        return shorten_url(argv[1])
    except IndexError:
        return 'Error: The URL was not provided.'

def askRun():
    url=str(raw_input('Insert the url that you want to shorten: '))
    return shorten_url(url)


try:
    if __name__ == '__main__':
        print sysRun()
except KeyboardInterrupt:
    print '\nThe progam was interrupted by keyboard.'