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

import builtins as __builtin__
import re
import keyword
if __name__=='__main__':
	from Graphics import Tkinter
else:
	from .Graphics import Tkinter

def any(name, alternates):
    "Return a named group pattern matching list of alternates."
    return "(?P<%s>" % name + "|".join(alternates) + ")"


def ty():
    kw = r"\b" + any("KEYWORD", keyword.kwlist) + r"\b"
    builtinlist = [str(name) for name in dir(__builtin__)
                                        if not name.startswith('_')]
    builtinlist.remove('print')
    builtin = r"([^.'\"\\#]\b|^)" + any("BUILTIN", builtinlist) + r"\b"
    comment = any("COMMENT", [r"#[^\n]*"])
    stringprefix = r"(\br|u|ur|R|U|UR|Ur|uR|b|B|br|Br|bR|BR)?"
    sqstring = stringprefix + r"'[^'\\\n]*(\\.[^'\\\n]*)*'?"
    dqstring = stringprefix + r'"[^"\\\n]*(\\.[^"\\\n]*)*"?'
    sq3string = stringprefix + r"'''[^'\\]*((\\.|'(?!''))[^'\\]*)*(''')?"
    dq3string = stringprefix + r'"""[^"\\]*((\\.|"(?!""))[^"\\]*)*(""")?'
    string = any("STRING", [sq3string, dq3string, sqstring, dqstring])
    return kw + "|" + builtin + "|" + comment + "|" + string +\
           "|" + any("SYNC", [r"\n"])

def _coordinate(start,end,string):
    srow=string[:start].count('\n')+1 # starting row
    scolsplitlines=string[:start].split('\n')
    if len(scolsplitlines)!=0:
        scolsplitlines=scolsplitlines[len(scolsplitlines)-1]
    scol=len(scolsplitlines)# Ending Column
    lrow=string[:end+1].count('\n')+1
    lcolsplitlines=string[:end].split('\n')
    if len(lcolsplitlines)!=0:
        lcolsplitlines=lcolsplitlines[len(lcolsplitlines)-1]
    lcol=len(lcolsplitlines)+1# Ending Column
    return '{}.{}'.format(srow, scol),'{}.{}'.format(lrow, lcol)#, (lrow, lcol)

def coordinate(pattern, string,txt):
    line=string.splitlines()
    start=string.find(pattern)  # Here Pattern Word Start
    end=start+len(pattern) # Here Pattern word End
    srow=string[:start].count('\n')+1 # starting row
    scolsplitlines=string[:start].split('\n')
    if len(scolsplitlines)!=0:
        scolsplitlines=scolsplitlines[len(scolsplitlines)-1]
    scol=len(scolsplitlines)# Ending Column
    lrow=string[:end+1].count('\n')+1
    lcolsplitlines=string[:end].split('\n')
    if len(lcolsplitlines)!=0:
        lcolsplitlines=lcolsplitlines[len(lcolsplitlines)-1]
    lcol=len(lcolsplitlines)# Ending Column
    return '{}.{}'.format(srow, scol),'{}.{}'.format(lrow, lcol)#, (lrow, lcol)

def check(k={}):
    if k['COMMENT']!=None:
    	return 'comment','red'
    elif k['BUILTIN']!=None:
    	return 'builtin','VioletRed'
    elif k['STRING']!=None:
    	return 'string','green'
    elif k['KEYWORD']!=None:
    	return 'keyword','orange'
    else:
    	return 'ss','NILL'

txtfilter=re.compile(ty(),re.S)


class ColorLight:
    def __init__(self, txtbox=None):
        self.txt=txtbox
        self.txt.bind("<Any-KeyPress>", self.trigger)

    def binding_functions_configuration(self):
        self.txt.storeobj['ColorLight']=self.trigger
        return

    def trigger(self, event=None):
        val=self.txt.get('1.0','end')
        if len(val)==1:
            return
        for i in ['comment','builtin','string','keyword']:
            self.txt.tag_remove(i,'1.0','end')
        for i in txtfilter.finditer(val):
            start=i.start()
            end=i.end()-1
            #print start,end
            tagtype,color=check(k=i.groupdict())
            if color!='NILL':
                ind1,ind2=_coordinate(start,end,val)
                #print ind1, ind2
                self.txt.tag_add(tagtype,ind1, ind2)
                self.txt.tag_config(tagtype,foreground=color)
                #Tkinter.Text.tag_configure
#        for i in idprog.finditer(val):
#            start=i.start()
#            end=i.end()-1
#            ind1,ind2=_coordinate(start,end,val)
#            self.txt.tag_add('BLUE',ind1, ind2)
#            self.txt.tag_config("BLUE",foreground='grey')
#            #Tkinter.Text.tag_configure

if __name__ == '__main__':
    root=Tkinter.Tk()
    txt=Tkinter.Text(root)
    txt.pack(expand='yes')
    txt.storeobj={}
    store=ColorLight(txtbox=txt)
    Tkinter.Button(root, text='Click me', command=lambda:store.trigger()).pack()
    root.mainloop()
