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
        self.function_binding_keys()
        self.other_functions_for_bindings()
        self.reset_functionals_for_bindings()


    def function_binding_keys(self):
        """
        Here, Add All Keys String For Bindings.
        """
        self.text.bind('<Control-A>', self.selectall)
        self.text.bind('<Control-a>', self.selectall)
        self.text.bind('<Control-Shift-z>', self.redo)
        self.text.bind('<Control-Shift-Z>', self.redo)
        return

    def reset_functionals_for_bindings(self):
        
        return

    def other_functions_for_bindings(self):
        self.text.tag_configure('selected', background='ivory2')
        return

    def cut(self, event=None):
        self.text.event_generate("<<Cut>>")
        return

    def copy(self, event=None):
        self.text.event_generate("<<Copy>>")
        print self.text.tag_ranges("selected")
        return

    def paste(self, event=None):
        self.text.event_generate("<<Paste>>")
        return

    def undo(self, event=None):
        self.text.event_generate('<<Undo>>')
        return

    def redo(self, event=None):
        self.text.event_generate("<<Redo>>")
        return

    def selectall(self, event=None):
        self.text.tag_add('selected','1.0','end')
        return

if __name__ == '__main__':
    root = Tkinter.Tk()
    pad = Tkinter.Text(root,wrap='none')
    StationeryFunctions(pad)
    pad.pack()
    root.mainloop()