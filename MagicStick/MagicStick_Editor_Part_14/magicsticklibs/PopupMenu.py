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

if __name__=='__main__':
	from Graphics import Tkinter 
else:
	from .Graphics import Tkinter

class Popup:
	def __init__(self, text):
		self.text = text
		self.functions_binding_key()
		self.functions_configurations()

	def functions_configurations(self):
		self.menu = Tkinter.Menu(self.text)
		self.menu.add_command(label="Copy", command=self.text.storeobj['Copy'])
		self.menu.add_command(label="Cut", command=self.text.storeobj['Cut'])
		self.menu.add_command(label="Paste", command=self.text.storeobj['Paste'])
		self.menu.add_separator()
		self.menu.add_command(label="Select All", command=self.text.storeobj['SelectAll'])
		self.menu.add_separator()
		return

	def functions_binding_key(self):
		self.text.bind("<Button-3>",self.show_menu_)

		return

	def show_menu_(self, event):
		self.menu.tk_popup(event.x_root, event.y_root)
		
		return

if __name__ == '__main__':
	root = Tkinter.Tk()
	text = Tkinter.Text()
	text.pack()
	text.storeobj={'SelectAll':None,
	"Copy":None,
	"Cut":None,
	"Paste":None}
	Popup(text)
	root.mainloop()
