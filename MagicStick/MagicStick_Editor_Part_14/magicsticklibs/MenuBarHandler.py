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

"""
SelectAll
DeselectAll
OpenFile
Cut
Redo
SaveAs
Save
Root
Undo
FindAll
FontChooser
ReplaceAll
OpenNew
ConfigApply
SaveConfig
Open
ResetTags
Copy
Paste
Find
Replace

"""


class MenuBar:
	def __init__(self, text):
		self.text = text
		self.create_menubar()

	def create_menubar(self):
		self.bar = Tkinter.Menu(self.text.storeobj['Root'])


		# Creating Sub menu
		sub_menu=Tkinter.Menu(self.bar, tearoff=0)
		self.bar.add_cascade(label='File', menu=sub_menu)

		sub_menu.add_command(label="New", accelerator="Ctrl+N",compound="left", underline=0, command=self.text.storeobj['OpenNew'])
		sub_menu.add_command(label="Open", accelerator="Ctrl+O",compound="left", underline=0, command=self.text.storeobj['Open'])
		sub_menu.add_separator()
		sub_menu.add_command(label="Save", accelerator="Ctrl+S",compound="left", underline=0, command=self.text.storeobj['Save'])
		sub_menu.add_command(label="Save As", accelerator="Ctrl+Shift+S",compound="left", underline=0, command=self.text.storeobj['SaveAs'])
		sub_menu.add_separator()
		sub_menu.add_command(label="Quit", accelerator="Ctrl+Q",compound="left", underline=0, command=self.text.storeobj['Quit'])

		# Creating Sub menu
		sub_menu=Tkinter.Menu(self.bar, tearoff=0)
		self.bar.add_cascade(label='Edit', menu=sub_menu)

		sub_menu.add_command(label="Redo", accelerator="Ctrl+Shift+Z",compound="left", underline=0, command=self.text.storeobj['Redo'])
		sub_menu.add_command(label="Undo", accelerator="Ctrl+Z",compound="left", underline=0, command=self.text.storeobj['Undo'])
		sub_menu.add_separator()
		sub_menu.add_command(label="Copy", accelerator="Ctrl+C",compound="left", underline=0, command=self.text.storeobj['Copy'])
		sub_menu.add_command(label="Cut", accelerator="Ctrl+X",compound="left", underline=0, command=self.text.storeobj['Cut'])
		sub_menu.add_command(label="Paste", accelerator="Ctrl+P",compound="left", underline=0, command=self.text.storeobj['Paste'])
		sub_menu.add_separator()
		sub_menu.add_command(label="Select All", accelerator="Ctrl+A",compound="left", underline=0, command=self.text.storeobj['SelectAll'])
		sub_menu.add_command(label="Deselect All", accelerator="",compound="left", underline=0, command=self.text.storeobj['DeselectAll'])
		

		# Creating Sub menu
		sub_menu=Tkinter.Menu(self.bar, tearoff=0)
		self.bar.add_cascade(label='Find', menu=sub_menu)

		sub_menu.add_command(label="Find", accelerator="Ctrl+F",compound="left", underline=0, command=self.text.storeobj['Find'])
		sub_menu.add_command(label="Find All", accelerator="Ctrl+Shift+F",compound="left", underline=0, command=self.text.storeobj['FindAll'])
		sub_menu.add_separator()
		sub_menu.add_command(label="Replace", accelerator="Ctrl+H",compound="left", underline=0, command=self.text.storeobj['Replace'])
		sub_menu.add_command(label="Replace All", accelerator="Ctrl+Shift+H",compound="left", underline=0, command=self.text.storeobj['ReplaceAll'])
		
		# Creating Sub menu
		sub_menu=Tkinter.Menu(self.bar, tearoff=0)
		self.bar.add_cascade(label='Prefrence', menu=sub_menu)

		sub_menu.add_command(label="Font", accelerator="Ctrl+F1",compound="left", underline=0, command=self.text.storeobj['FontChooser'])
		sub_menu.add_separator()
		sub_menu.add_command(label="Settings", accelerator=" ",compound="left", underline=0, command=self.text.storeobj['OpenNew'])
		
		# Creating Sub menu
		sub_menu=Tkinter.Menu(self.bar, tearoff=0)
		self.bar.add_cascade(label='Help', menu=sub_menu)

		sub_menu.add_command(label="Plugins", accelerator="",compound="left", underline=0, command=self.text.storeobj['OpenNew'])
		sub_menu.add_command(label="Author", accelerator="",compound="left", underline=0, command=self.text.storeobj['OpenNew'])
		





		self.text.storeobj['Root'].configure(menu=self.bar)
		
		
		return

if __name__ == '__main__':
	root= Tkinter.Tk()
	pad=Tkinter.Text(root)
	pad.pack()
	pad.storeobj={"Root":root}
	MenuBar(pad)
	root.mainloop()

