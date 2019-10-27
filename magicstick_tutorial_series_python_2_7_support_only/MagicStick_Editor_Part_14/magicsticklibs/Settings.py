#!/usr/bin/python
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
import os
import shelve
try:
	mod = __import__("dbm")
except:
	mod = __import__('gdbm')

Settings ={

'background':'white', 

'borderwidth':2, 

'cursor':"xterm",


"font":("arial", 15),

"foreground":"black",


"highlightbackground":"white",

"highlightcolor":"blue",

"highlightthickness":4, 

"padx":5, 

"pady":5,

"relief":"flat",

"selectbackground" : "skyblue",

"selectborderwidth":0, 

"selectforeground":"black",

"spacing1":1, # Between Two Lines

"spacing2":1, 

"spacing3":1,

"state":"normal", 

"tabs":"1c", 

"takefocus":True,


}




Config_file_database="Settings.dbm"


class MagicStickSettings:
	def __init__(self, *args, **kwargs):
		self.filename=Config_file_database		
		self.dataobj=Settings
		if not os.path.exists(self.filename):
			self.write(self.dataobj)

	def write(self, args):
		if os.path.exists(self.filename):
			self.update(args)
		else:
			storeobj = shelve.Shelf(mod.open(self.filename,'c'))
			for key,item in self.dataobj.items():
				storeobj[key]=item
			storeobj.close()
		return

	def read(self, args):
		if os.path.exists(self.filename):
			storeobj = shelve.Shelf(mod.open(self.filename,'c'))
			data=storeobj[args]
			storeobj.close()
		return data

	def readall(self):
		if os.path.exists(self.filename):
			storeobj = shelve.Shelf(mod.open(self.filename,'c'))
			data=list(storeobj.items())
			storeobj.close()
		
		return data


	def update(self, args):
		if args:
			storeobj = shelve.Shelf(mod.open(self.filename,'c'))
			for key,item in args.items():
				storeobj[key]=item
			storeobj.close()
		return

	def delete(self, args):
		if args:
			storeobj = shelve.Shelf(mod.open(self.filename,'c'))
			del storeobj[args]
			storeobj.close()		
		return

	def __setitem__(self, *args):
		self.write({args[0]:args[1]})
		return

	def __getitem__(self, args):
		return self.read(args)

	def __repr__(self):
		return "<MagicStick-Configuration-settings-Handler>"

	def __delitem__(self, args):
		return self.delete(args)


class Configuration:
	def __init__(self, text):
		self.text = text
		self.db=MagicStickSettings()
		self.apply()
		self.text.storeobj['ConfigApply']=self.apply
		self.text.storeobj['SaveConfig']=self.retrieve
		# To Use This option, You Need Small Modification in "TextPad.py"
		# Change from "self.storeobj = {}"
		# to
		# "self.storeobj = {"Root", self.master}"
		#
		self.text.storeobj['Root'].wm_protocol('WM_DELETE_WINDOW',self.retrieve)
		

	def apply(self, event=None):

		print("Loading Settings...")
		value = dict(self.db.readall())
		self.text.configure(**value)
		return

	def retrieve(self, event=None):
		print("Saving Settings...")
		value = dict(self.db.readall())
		for key, value in value.items():
			cvalue = self.text.cget(key)
			#print key, cvalue
			if key=="tabs":
				cvalue="1c"
			self.db[key]=cvalue
		if "Quit" in list(self.text.storeobj.keys()):
			self.text.storeobj['Quit']()
		return

		




if __name__ == '__main__':
	from .Graphics import Tkinter
	root = Tkinter.Tk()
	pad = Tkinter.Text(root)
	pad.pack()
	pad.storeobj={"Root":root}
	#pad.configure(**Settings)
	Configuration(pad)
	root.mainloop()
