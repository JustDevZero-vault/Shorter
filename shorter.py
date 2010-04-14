#!/usr/bin/env python
# -*- coding: utf-8 -*-



#       pyly.py written in python2.8
#       version 1.4
#       Copyright 2010 Mephiston <meph.snake@gmail.com>
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

#------------------------------ Utilities --------------------------------------- #
# The main purpose of this script is to easily give urls with bit.ly service.
# It shorts the url anonymously.
#---------------------------- ToDo LIST ------------------------------------ #
#       Include more Shorter url services.
#--------------------------- CHANGE LOG ----------------------------------------- #
#       1.0     Initial release

from wx import Frame,ICONIZE,CAPTION,MINIMIZE,MINIMIZE_BOX,MAXIMIZE_BOX,CLOSE_BOX,SYSTEM_MENU,RESIZE_BORDER,CLIP_CHILDREN,TextCtrl,ComboBox,Button,EVT_BUTTON,ImageFromStream,BitmapFromImage,EmptyIcon,TheClipboard, InitAllImageHandlers,App,CB_DROPDOWN,CB_SORT,CB_READONLY,BU_TOP,ID_COPY,BoxSizer,LEFT,RIGHT,ALL,EXPAND,SHAPED,VERTICAL,HORIZONTAL,MessageBox,TextDataObject

from base64 import b64decode
from cStringIO import StringIO
from urllib import urlopen

AnonymousBitlyFlag = True

try:
    from apyly import shorten_url as shorten_apyly,splitter
except ImportError:
    AnonymousBitlyFlag = False

# begin wxGlade: extracode
# end wxGlade


#GLOBAL STUFF

def getImageStream():
    favicon_png_b64='''\
    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
    AAAAAElFTkSuQmCC
    '''

    favicon_png_bytes=b64decode(favicon_png_b64)
    # convert to png image bytes
    png_favicon_stream=StringIO(favicon_png_bytes)
    # convert png bytes to data stream
    return favicon_png_bytes




class BitLyFrame(Frame):
    def __init__(self, *args, **kwds):
        choices = []
        if AnonymousBitlyFlag:
            choices.append("bit.ly (anonymous)")
        choices.sort()

        # begin wxGlade: BitLyFrame.__init__
        kwds["style"] = ICONIZE|CAPTION|MINIMIZE|CLOSE_BOX|MINIMIZE_BOX|MAXIMIZE_BOX|SYSTEM_MENU|RESIZE_BORDER|CLIP_CHILDREN
        Frame.__init__(self, *args, **kwds)
        self.SelectBox = ComboBox(self, 0, choices=choices, style=CB_DROPDOWN|CB_SORT|CB_READONLY)
        self.OriginalTextBox = TextCtrl(self, 2, value="Enter your bad long url here.")
        self.ShortUrlBox = TextCtrl(self, 1, value="")

        self.ShortenButton = Button(self, 4, _("Short It!"), style=BU_TOP)
        EVT_BUTTON(self.ShortenButton, 4, self.OnShortenButton)

        self.CopyButton = Button(self, ID_COPY, "", style=BU_TOP)
        self.CopyButton.Bind(EVT_BUTTON, self.OnCopyButton)

        myStream = StringIO(getImageStream())
        myImage = ImageFromStream(myStream)
        myBitmap = BitmapFromImage(myImage)
        myIcon = EmptyIcon()
        myIcon.CopyFromBitmap(myBitmap)
        self.SetIcon(myIcon)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: BitLyFrame.__set_properties
        self.SetTitle(_("GeeklyShorter"))
        self.SetSize((575, 147))
        self.SelectBox.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: BitLyFrame.__do_layout
        FirstSizer = BoxSizer(VERTICAL)
        sizer_1 = BoxSizer(HORIZONTAL)
        FirstSizer.Add(self.SelectBox, 0, ALL, 6)
        FirstSizer.Add(self.OriginalTextBox, 0, ALL|EXPAND, 6)
        FirstSizer.Add(self.ShortUrlBox, 0, ALL|EXPAND, 6)
        sizer_1.Add(self.ShortenButton, 0, LEFT|RIGHT, 100)
        sizer_1.Add(self.CopyButton, 0, LEFT|RIGHT, 100)
        FirstSizer.Add(sizer_1, 1, SHAPED, 0)
        self.SetSizer(FirstSizer)
        self.Layout()
        # end wxGlade


    def OnShortenButton(self, event):
        shorter = self.SelectBox.GetValue()
        url = self.OriginalTextBox.GetValue()
        if shorter == "bit.ly (anonymous)":
            shortened=shorten_apyly(url)
        elif shorter =="":
            shortened="No shorteners found."

        if (shortened=="The URL was not recognized."):
            MessageBox("The URL was not recognized.", "Error")
        elif (shortened=="The URL was not provided."):
            MessageBox("The URL was not provided.", "Error")
        elif (shortened=="No shorteners found."):
            MessageBox("No shorteners found.", "Error")
        else:
            self.ShortUrlBox.SetValue(shorten_apyly(url))

    def OnCopyButton(self, event):
        text = self.ShortUrlBox.GetValue()
        self.do = TextDataObject()
        self.do.SetText(text)
        if TheClipboard.Open():
            TheClipboard.SetData(self.do)
            TheClipboard.Close()
            #status = "Copied %s to clipboard" % text
            #print status
        else:
            MessageBox("Unable to open the clipboard", "Error")

# end of class BitLyFrame


class MyApp(App):
    def OnInit(self):
        InitAllImageHandlers()
        FirstFrame = BitLyFrame(None, -1, "")
        self.SetTopWindow(FirstFrame)
        FirstFrame.Show()
        return 1

# end of class MyApp

if __name__ == "__main__":
    import gettext
    gettext.install("GeeklyShorter") # replace with the appropriate catalog name

    GeeklyShorter = MyApp(0)
    GeeklyShorter.MainLoop()
