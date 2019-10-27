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


from Graphics import Tkinter

def FindAsk(parent,*args):
	root = Tkinter.Toplevel(parent)
	root.title("Find And Replace")
	root.transient(parent)
	root.focus_force()
	root.resizable(width=0, height=0)
	root['padx']=20
	fields = {}
	field={}
	for r, label in enumerate(args):
		store_label = Tkinter.Label(root, text=label)
		store_label.grid(row=r, column = 0, ipady=5, ipadx=20)
		store_entry = Tkinter.Entry(root)
		store_entry.grid(row=r, column=1)
		field[label]=store_entry
	fields['submit']=False
	def sub():
		for l,t in field.iteritems():
			fields[l]=t.get()
		fields['submit']=True
		root.destroy()
		return
	submit=Tkinter.Button(root,text="Ok", command=sub)
	submit.grid(row=r+1, column=2)
	root.wait_window()
	return fields


class FindReplaceFunctions:
	def __init__(self,text):
		self.text = text
		self.key_binding_functions()
		self.binding_functions_configuration()

	def binding_functions_configuration(self):
		self.text.storeobj['Find'] = self.find_
		self.text.storeobj['FindAll'] = self.find_all
		self.text.storeobj['Replace'] = self.replace
		self.text.storeobj['ReplaceAll'] = self.replace_all
		self.text.storeobj['ResetTags']=self.reset_tags
		return


	def key_binding_functions(self):
		for key in ['<Control-F>',"<Control-f>"]:
			self.text.bind(key, self.find_)
		for key in ['<Control-Shift-F>',"<Control-Shift-f>"]:
			self.text.bind(key, self.find_all)
		for key in ['<Control-Shift-H>',"<Control-Shift-h>"]:
			self.text.bind(key, self.replace_all)
		for key in ['<Control-H>',"<Control-h>"]:
			self.text.bind(key, self.replace)
		for key in ['<Any-Button>']:
			self.text.bind(key, self.reset_tags)
		return

	def _search_(self, word):
		self.text.tag_delete("search")
		if word:
			countvar = Tkinter.StringVar()
			f = self.text.search(word, "1.0", count=countvar)
			starting_index = f
			ending_index = "{}+{}c".format(starting_index, countvar.get())
			self.text.tag_add("search", starting_index, ending_index)
			self.text.tag_configure("search", background="skyblue", foreground="red")
			return True
		else:
			return None

	def reset_tags(self, event=None):
		self.text.tag_delete("search")
		return

	def _search_all_(self, word):
		self.text.tag_delete("search")
		index="1.0"
		if word:
			while True:
				f = self.text.search(word, index, stopindex=Tkinter.END)
				if not f:
					break
				starting_index =int(f.split(".")[0])
				ending_index  = len(word)+int(f.split(".")[1])
				coordinates = "{}.{}".format(starting_index, ending_index)
				self.text.tag_add("search", f, coordinates)
				self.text.tag_configure("search", background="skyblue", foreground="red")
				index = coordinates
			return True
		else:
			return None


	def find_(self, event=None):
		t = FindAsk(self.text.master, "Find")
		if t['submit']:
			self._search_(t['Find'])
		return

	def find_all(self, event=None):
		t = FindAsk(self.text.master, "FindAll")
		if t['submit']:
			self._search_all_(t['FindAll'])
		return

	def replace(self, event=None):
		t = FindAsk(self.text.master, "Find", "Replace")
		if t['submit']:
			print t['Find']
			print t['Replace']
		return

	def replace_all(self, event=None):
		t = FindAsk(self.text.master, "FindAll", "ReplaceAll")
		if t['submit']:
			print t['FindAll']
			print t['ReplaceAll']
		return


if __name__ == '__main__':
	root = Tkinter.Tk()
	pad = Tkinter.Text(root)
	pad.pack()
	pad.storeobj={}
	FindReplaceFunctions(pad)
	#print FindAsk(root,"a","b",1)
	root.mainloop()