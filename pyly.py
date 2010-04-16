#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlopen,urlencode
from exceptions import IndexError, IOError, KeyError
from sys import argv
from re import match
#       pyly.py written in python2.6
#       version 1.6
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
# It shorts the url with your user and apikey for having stadistics and all the benefits of registered.
#--------------------------- CHANGE LOG ----------------------------------------- #
#       1.0     Initial release
#       1.1     Fixed bugs, can use url with "&" atributes
#       1.2     Added a system argument function, you can choose between the sys.argv or ask function.
#               By changing the line 75 for sysRun(key,user) or askRun(key,user)
#       1.3     Fixed bugs, errors are treated as exceptions.
#       1.4     Some prints become "returns", because it allows to use it externally
#       1.5     The key and user are out of the main, for using with the GUI TOOL. geekshort.py
#       1.6     Fixed bugs, ignores not url strings (http* *ftp*).
#--------------------------- TESTED IN ------------------------------------------ #
#       GNU/Linux (all distros)     WINDOWS NT*         MacOSX      *BSD


#GLOBAL STUFF
key=str('ENTER_YOUR_API_KEY_HERE')
user=str('ENTER_YOUR_USER_HERE')

def check_url(long_url):
    if match("^https?://[^ ]+|^ftp?://[^ ]+|^sftp?://[^ ]+", long_url):
        return True
    else:
        return False

def shorten_url(long_url, api_key, my_user):
    if check_url(long_url):
        try:
            longUrl=urlencode(dict(longUrl=long_url))
            apiKey=urlencode(dict(apiKey=api_key))
            login=urlencode(dict(login=my_user))
            encodeurl='http://api.bit.ly/shorten?version=2.0.1&%s&%s&%s' % (longUrl, apiKey, login)
            request=urlopen(encodeurl)
            responde=request.read ()
            request.close()
            respondedict=eval(responde)
            #Here we make the requesting process.
            try:
                short_url=respondedict["results"][long_url]["shortUrl"]
                return short_url
            except KeyError:
                return 'Error: The URL entered was not valid.'
                #If the url is not recognized on the request, we treat it as an error.
        except IOError, e:
            return 'Error: An I/O error happened.'
    else:
        return "Error: The URL was not provided."
def askRun(key,user):
    urll=str(raw_input('Insert the url that you want to shorten: '))
    return shorten_url(urll, key, user)

def sysRun(key,user):
    #If you chose sysRun, it will use the url provided in your command line.
    try:
        return shorten_url(argv[1], key, user)
    except IndexError:
        return 'Error: The URL was not provided.'



try:
    if __name__ == '__main__':
        if (key=='ENTER_YOUR_API_KEY_HERE'):
            print 'Error: You forgot to specify your API KEY.'
        if (user=='ENTER_YOUR_USER_HERE'):
            print 'Error: You forgot to specify your USER.'
        else:
            print sysRun(key,user)
except KeyboardInterrupt:
    print '\nThe progam was interrupted by keyboard.'