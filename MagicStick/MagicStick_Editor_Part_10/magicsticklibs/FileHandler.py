#!/usr/bin/python
##
##
##    Developed by:   Suraj Singh
##                    surajsinghbisht054@gmail.com
##					  github.com/surajsinghbisht054
## 					  http://bitforestinfo.blogspot.com
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
##					  github.com/surajsinghbisht054
## 					  http://bitforestinfo.blogspot.com nor
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
from Graphics import Tkinter, tkFileDialog

class FileHandler:
	def __init__(self, text):
		self.text = text
		self.text.storeobj['OpenFile']=None
		self.functions_key_bindings()
		self.binding_key_configuration()

	def binding_key_configuration(self):
		for key in ['<Control-N>',"<Control-n>"]:
			self.text.bind(key, self.new_file)
		for key in ['<Control-S>',"<Control-s>"]:
			self.text.bind(key, self.save_file)
		for key in ['<Control-Shift-S>',"<Control-Shift-s>"]:
			self.text.bind(key, self.save_as)
		for key in ['<Control-O>',"<Control-o>"]:
			self.text.bind(key, self.open_file)
		for key in ['<Control-q>',"<Control-Q>"]:
			self.text.bind(key, self.quit)
		return

	def functions_key_bindings(self):
		self.text.storeobj['Open']=self.open_file
		self.text.storeobj['Save']=self.save_file
		self.text.storeobj['SaveAs']=self.save_as
		self.text.storeobj['OpenNew']=self.new_file
		return

	def open_file(self, event=None):
		path = tkFileDialog.askopenfilename()
		if path:
			data=open(path,"rb").read()
			self.text.delete('1.0','end')
			self.text.insert("1.0", data)
			self.text.storeobj['OpenFile']=path
		return

	def save_file(self, event=None):
		if not self.text.storeobj['OpenFile']:
			path = tkFileDialog.asksaveasfilename()
		else:
			path = self.text.storeobj['OpenFile']
		if path:
			data = self.text.get("1.0",'end')
			f_=open(path,"wb")
			f_.write(data)
			f_.close()
			self.text.storeobj['OpenFile']=path
		return

	def save_as(self, event=None):
		path = tkFileDialog.asksaveasfilename()
		if path:
			data = self.text.get("1.0",'end')
			f_=open(path,"wb")
			f_.write(data)
			f_.close()
		return

	def new_file(self, event=None):
		print "New"
		return

	def quit(self, event=None):
		import sys
		sys.exit(0)
		return



if __name__ == '__main__':
	root = Tkinter.Tk()
	pad = Tkinter.Text(root)
	pad.pack()
	pad.storeobj={}
	FileHandler(pad)
	root.mainloop()