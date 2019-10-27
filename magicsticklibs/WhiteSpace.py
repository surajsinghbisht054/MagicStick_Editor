
import Tkinter
import re

class Space:
	def __init__(self, text):
		self.text = text
		self.filter=re.compile("(\t*)(.+)(:\n)")
		self.active_tabs=0
		self.text.bind("<Return>", self.Check_Space)

	def Check_Space(self, event=None):
		print event.x, event.y
		self.get_tabs()
		return

	def get_tabs(self):
		data = self.filter.findall(self.text.get("current linestart", "end"))
		print data
		if data:
			t=len(data[0][0])+1
			self.active_tabs=t
			self.insert_tab(tab=self.active_tabs)
		return

	def insert_tab(self, tab=0):
		#print "Inserting Tab"
		#k=self.text.index("end")
		self.text.insert('insert wordstart',''+'-'*tab)#"insert linestart","insert lineend+1c"
		#self.text.mark_set("insert",self.text.index("insert wordstart-1c"))
		return

if __name__ == '__main__':
	root = Tkinter.Tk()
	pad = Tkinter.Text(root)
	pad.pack()
	pad.storeobj={}
	Space(pad)
	#FileHandler(pad)
	root.mainloop()
