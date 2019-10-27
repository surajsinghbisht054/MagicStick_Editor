#!/usr/bin/python
##
##
##    Developed by:   Suraj Singh
##                    surajsinghbisht054@gmail.com
##                    github.com/surajsinghbisht054
##                    http://bitforestinfo.blogspot.com
##
##    Permission is hereby granted, free of charge, to any person obtaining
##    a copy of this software and associated documentation files (the
##    "Software"), to deal with the Software without restriction, including
##    without limitation the rights to use, copy, modify, merge, publish,
##    distribute, sublicense, and/or sell copies of the Software, and to
##    permit persons to whom the Software is furnished to do so, subject to
##    the following conditions:
##
##    + Redistributions of source code must retain the above copyright
##      notice, this list of conditions and the following disclaimers.
##
##    + Redistributions in binary form must reproduce the above copyright
##      notice, this list of conditions and the following disclaimers in the
##      documentation and/or other materials provided with the distribution.
##
##    + Neither the names of Suraj Singh
##                    surajsinghbisht054@gmail.com
##                    github.com/surajsinghbisht054
##                    http://bitforestinfo.blogspot.com nor
##      the names of its contributors may be used to endorse or promote
##      products derived from this Software without specific prior written
##      permission.
##
##    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
##    OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
##    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
##    IN NO EVENT SHALL THE CONTRIBUTORS OR COPYRIGHT HOLDERS BE LIABLE FOR
##    ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
##    CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
##    THE SOFTWARE OR THE USE OR OTHER DEALINGS WITH THE SOFTWARE.
##
##
## ################################################
## ###### Please Don't Remove Author Name #########
## ############# Thanks ###########################
## ################################################
##
##
__author__='''

######################################################
                By S.S.B Group                          
######################################################

    Suraj Singh
    Admin
    S.S.B Group
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/

    Note: We Feel Proud To Be Indian
######################################################
'''
from Graphics import Tkinter
from Graphics import tkFont, ttk
import time
from threading import Thread

WIDTH=250
HEIGHT=150
class Banner:
	def __init__(self, widget, text, width=None, height=None):
		self.widget = widget
		self.text = text
		self.FocusLine = False
		self.window = None
		self.width=width
		self.height=height
		self.MouseBindings()

	def AutoHide(self):
		time.sleep(5)
		self.HideInfo()
		return

	def MouseBindings(self):
		# Show Banner
		for key in ['<Enter>']:
			self.widget.bind(key, self.ShowInfo)
		
		for key in ['<Leave>']:
			self.widget.bind(key, self.HideInfo)
		return
		


	def HideInfo(self, event=None):
		if self.window:
			self.window.destroy()
			self.window=None
		return

	def ShowInfo(self, event=None):
		if not self.window:
			self.window=Tkinter.Toplevel()
			self.window.overrideredirect(True)
			WIDTH = self.width or len(self.text)*10
			HEIGHT = self.height or (len(self.text.split('\n'))+1)*10
			self.window.geometry("%dx%d+%d+%d" % (WIDTH,HEIGHT,
				event.x_root+10,
				event.y_root+10
				))
			Label=Tkinter.Label(self.window, text=self.text, font=("arial 10 bold"), fg='white', bg='black')
			Label.pack(expand=True, fill='both')
			self.window.wait_visibility(self.window)
			self.window.attributes('-alpha',0.7)
			t= Thread(target=self.AutoHide)
			t.start()
		return

if __name__=='__main__':       
	root = Tkinter.Tk()
	Button = Tkinter.Button(root, text="Point Mouse Here")
	Button.pack(padx=20, pady=20)
	Banner(Button, """Testing Windows""")
	root.mainloop()
