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
import re
import keyword


codes = " and   as   assert   break   class   continue   def   del   elif   else   except   exec   finally   for   from   global   if   import   in   is   lambda   not   or   pass   print   raise   return   try   while   with   yield "


class AutoComplete:
	def __init__(self, pad):
		self.text = pad
		self.s = None
		self.text.bind("<KeyRelease>", self.check)

	def check(self, event=None):
		print event.x, event.y
		word = self.text.get("insert linestart","insert wordend").split(" ")[-1]
		x,y = self.text.winfo_pointerxy()
		print x,y
		#self.ShowSuggestion(x,y,Data, self.GetSuggestion(Data))
		#print Data
		return

	
	def GetSuggestion(self, hint):
		engine = re.compile('\S'+hint+"\S+")
		return engine.findall(self.text.get("1.0","end")+codes)

	def ShowSuggestion(self,x, y, hint ,suggestions):
		if self.s:
			print "DEstroy"
			self.s.destroy()
		if suggestions:
			Top=Tkinter.Toplevel(self.text.master)
			l=Tkinter.Listbox(Top, bg="black", fg='white')
			l.pack(expand=True, fill='both')
			Top.geometry("+%d+%d" % (x, y))
			for i in suggestions:
				l.insert('end',i)
			Top.overrideredirect(True)
			self.s = Top
			#self.s.focus()
		return



if __name__ == '__main__':
	root = Tkinter.Tk()
	t= Tkinter.Text(root)
	t.pack()
	AutoComplete(t)



	root.mainloop()
