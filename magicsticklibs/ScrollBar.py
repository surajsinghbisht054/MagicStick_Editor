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
    Suraj Singh
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/
'''

if __name__=='__main__':
	from Graphics import Tkinter 
else:
	from .Graphics import Tkinter 

class Scrollbar:
	def __init__(self,text):
		self.frame = text.master
		self.text = text
		self.text.configure(wrap='none')
		self.for_x_view()
		self.for_y_view()

	def for_x_view(self):
		# scroll Bar x For width
		scroll_x=Tkinter.Scrollbar(self.frame, orient='horizontal',command=self.text.xview)
		scroll_x.config(command=self.text.xview)
		self.text.configure(xscrollcommand=scroll_x.set)
		scroll_x.pack(side='bottom', fill='x', anchor='w')
		return

	def for_y_view(self):
		# Scroll Bar y For Height
		scroll_y = Tkinter.Scrollbar(self.frame)
		scroll_y.config(command=self.text.yview)
		self.text.configure(yscrollcommand=scroll_y.set)
		scroll_y.pack(side='right', fill='y')		
		return


if __name__ == '__main__':
	root = Tkinter.Tk()
	pad = Tkinter.Text(root,wrap='none')
	Scrollbar(pad)
	pad.pack()
	root.mainloop()
