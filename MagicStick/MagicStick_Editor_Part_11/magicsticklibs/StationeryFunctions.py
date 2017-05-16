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

class StationeryFunctions:
    def __init__(self, text):
        self.text = text
        self.create_binding_keys()
        self.binding_functions_config()
        self.join_function_with_main_stream()


    def join_function_with_main_stream(self):
        self.text.storeobj['Copy']   =  self.copy
        self.text.storeobj['Cut']    =  self.cut
        self.text.storeobj['Paste']  =  self.paste
        self.text.storeobj['Undo']   =  self.undo
        self.text.storeobj['Redo']   =  self.redo 
        self.text.storeobj['SelectAll']=self.select_all
        self.text.storeobj['DeselectAll']=self.deselect_all
        return

    def binding_functions_config(self):
        self.text.tag_configure("sel", background="skyblue")
        self.text.configure(undo=True,autoseparators=True, maxundo=-1)
        return

    def copy(self, event=None):
        self.text.event_generate("<<Copy>>")
        return

    def paste(self, event=None):
        self.text.event_generate("<<Paste>>")
        return

    def cut(self, event=None):
        self.text.event_generate("<<Cut>>")
        return

    def undo(self, event=None):
        self.text.event_generate("<<Undo>>")
        return

    def redo(self, event=None):
        self.text.event_generate("<<Redo>>")
        return

    def create_binding_keys(self):
        for key in ["<Control-a>","<Control-A>"]:
            self.text.master.bind(key, self.select_all)
        for key in ["<Button-1>","<Return>"]:
            self.text.master.bind(key, self.deselect_all)

        return

    def select_all(self, event=None):
        self.text.tag_add("sel",'1.0','end')
        return


    def deselect_all(self, event=None):
        self.text.tag_remove("sel",'1.0','end')
        return

if __name__ == '__main__':
    root = Tkinter.Tk()
    pad = Tkinter.Text(root,wrap='none')
    pad.storeobj = {}
    StationeryFunctions(pad)
    pad.pack()
    root.mainloop()