"""
Author: Rohan Dutta.
Usage: C Companion.py 
Description: A toolbox to fasten
             and simplify C programming
             in any IDE.
Version: 1.0
"""

import clipboard
import Tkinter
import tkMessageBox
from Tkinter import *
from PIL import Image, ImageTk
top = Tkinter.Tk()

top.wm_title("C COMPANION")
top.attributes("-topmost", True)
image = Image.open('4.JPG')
photo_image = ImageTk.PhotoImage(image)
Tkinter.Label(top, image = photo_image).place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor="nw")

def cv():
    t1=Lb1.get(Lb1.curselection());
    t2=p.get();
    if(t2[0].isdigit()):
        tkMessageBox.showerror("GUIDE", "Variable name must not start with digit")
    else:
        t3=t1+" "+t2+";"
        clipboard.copy(t3);
        top1 = Toplevel()
        top1.title('STATUS')
        Message(top1,text='Sucessful! Now paste it.').grid()
        top1.attributes("-topmost", True)
        top1.after(1000, top1.destroy)

def cv1():
    t1=Lb1.get(Lb1.curselection());
    t2=p.get();
    if(t2[0].isdigit()):
        tkMessageBox.showerror("GUIDE", "Variable name must not start with digit")
    else:
        t3=q.get();
        if (t3.isdigit()):
            t3=t1+" "+t2+"[{}];".format(t3);
            clipboard.copy(t3);
            top1 = Toplevel()
            top1.title('STATUS')
            Message(top1,text='Sucessful! Now paste it.').grid()
            top1.attributes("-topmost", True)
            top1.after(1000, top1.destroy)
        else:
            tkMessageBox.showerror("GUIDE", "The size must be an Interger")

def hdr():
    clipboard.copy('''#include<stdio.h>\n#include<stdlib.h>\n#include<string.h>\n#include<math.h>\n''')
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

def dm1():
    clipboard.copy('''if(){\n}''')
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

def dm2():
    t=clipboard.copy('''else{\n}''')
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

def dm3():
    t=clipboard.copy('''else if(){\n}''')
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

def dm4():
    t=clipboard.copy('''if()?():()''')
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

def dm5():
    t=clipboard.copy('''switch(){\ncase : break;\ndefault:;\n}''')
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

def floop():
     t1=p.get()
     t2=b.get()
     if (t2.isdigit()):
         t3=c.get()
         t4=d.get()
         t5="int";
         s="{} {}={};\nfor(;{}{};{}={}{})".format(t5,t1,t2,t1,t3,t1,t1,t4)+"{\n}"
         t=clipboard.copy(s)
         top1 = Toplevel()
         top1.title('STATUS')
         Message(top1,text='Sucessful! Now paste it.').grid()
         top1.attributes("-topmost", True)
         top1.after(1000, top1.destroy)
     else:
         tkMessageBox.showerror("GUIDE", "Initialize with Integer")

def wloop():
    t1=p.get()
    t2=b.get()
    if (t2.isdigit()):
        t3=c.get()
        t4=d.get()
        t5="int";
        s="{} {}={};\nwhile({}{})".format(t5,t1,t2,t1,t3)+"{\n"+"{}={}{};".format(t1,t1,t4)+"\n}"
        t=clipboard.copy(s)
        top1 = Toplevel()
        top1.title('STATUS')
        Message(top1,text='Sucessful! Now paste it.').grid()
        top1.attributes("-topmost", True)
        top1.after(1000, top1.destroy)
    else:
         tkMessageBox.showerror("GUIDE", "Initialize with Integer")

def dwloop():
    t1=p.get()
    t2=b.get()
    if (t2.isdigit()):
        t3=c.get()
        t4=d.get()
        t5="int";
        s="{} {}={};\ndo".format(t5,t1,t2)+"{"+"\n{}={}{};".format(t1,t1,t4)+"}"+"while({}{});".format(t1,t3);
        t=clipboard.copy(s)
        top1 = Toplevel()
        top1.title('STATUS')
        Message(top1,text='Sucessful! Now paste it.').grid()
        top1.attributes("-topmost", True)
        top1.after(1000, top1.destroy)
    else:
         tkMessageBox.showerror("GUIDE", "Initialize with Integer")

def inp():
    t1=p.get();
    t3=Lb1.get(Lb1.curselection());
    if(t3=='int'):
        t4='d'
    elif(t3=='float'):
        t4='f'
    elif(t3=='double'):
        t4='lf'
    elif(t3=='char'):
        t4='c'
    t2='scanf("%{}",&{});\n'.format(t4,t1)
    t=clipboard.copy(t2)
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)


def oup():
    t1=p.get();
    t3=Lb1.get(Lb1.curselection());
    if(t3=='int'):
        t4='d'
    elif(t3=='float'):
        t4='f'
    elif(t3=='double'):
        t4='lf'
    elif(t3=='char'):
        t4='c'
    t2='printf("%{}",{});\n'.format(t4,t1)
    t=clipboard.copy(t2)
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)


def main():
    t1="void main(){\n}"
    t=clipboard.copy(t1)
    top1 = Toplevel()
    top1.title('STATUS')
    Message(top1,text='Sucessful! Now paste it.').grid()
    top1.attributes("-topmost", True)
    top1.after(1000, top1.destroy)

    

Tkinter.Label(top,text="HEADER FILES:",font="bold").grid(row=0,column=0)
Tkinter.Button(top,height=1,width=10,text ="HEADERS", command = hdr).grid(row=0,column=1)
Tkinter.Button(top,height=1,width=10,text ="MAIN", command = main).grid(row=0,column=2)
Tkinter.Label(top,text="DATA TYPE",font="bold").grid(row=1,column=0)
Lb1 = Listbox(top,height=4)
Lb1.insert(1, "int")
Lb1.insert(2, "float")
Lb1.insert(3, "double")
Lb1.insert(4, "char")
Lb1.select_set(0);
Lb1.activate(0);
Lb1.grid(row=1,column=1)
Tkinter.Label(top,text="VARNAME",font="bold").grid(row=2,column=0)
p=Tkinter.Entry(top,bd=5)
p.grid(row=2,column=1)
Tkinter.Button(top,height=1,width=10,text ="VARIABLE", command = cv).grid(row=2,column=2)
Tkinter.Label(top,text="SIZE",font="bold").grid(row=3,column=0)
q=Tkinter.Entry(top,bd=5)
q.grid(row=3,column=1)
Tkinter.Button(top,height=1,width=10,text ="ARRAY", command = cv1).grid(row=3,column=2)
Tkinter.Label(top,text="DECISION MAKING",font="bold").grid(row=4,column=0)
Tkinter.Button(top,height=1,width=10,text ="IF", command = dm1).grid(row=4,column=1)
Tkinter.Button(top,height=1,width=10,text ="ELSE", command = dm2).grid(row=4,column=2)
Tkinter.Button(top,height=1,width=10,text ="ELSE IF", command = dm3).grid(row=5,column=0)
Tkinter.Button(top,height=1,width=10,text ="?:", command = dm4).grid(row=5,column=1)
Tkinter.Button(top,height=1,width=10,text ="SWITCH-CASE", command = dm5).grid(row=5,column=2)
Tkinter.Label(top,text="LOOP",font="bold").grid(row=6,column=1)
'''Tkinter.Label(top,text="VARNAME",font="italic").grid(row=7,column=0)
a=Tkinter.Entry(top,bd=5)
a.grid(row=7,column=1)'''
Tkinter.Label(top,text="INITIALIZE",font="italic").grid(row=8,column=0)
b=Tkinter.Entry(top,bd=5)
b.grid(row=8,column=1)
Tkinter.Label(top,text="TEST EXPRESSION",font="italic").grid(row=9,column=0)
c=Tkinter.Entry(top,bd=5)
c.grid(row=9,column=1)
Tkinter.Label(top,text="UPDATION",font="italic").grid(row=10,column=0)
d=Tkinter.Entry(top,bd=5)
d.grid(row=10,column=1)
Tkinter.Button(top,height=1,width=10,text ="FOR", command = floop).grid(row=11,column=0)
Tkinter.Button(top,height=1,width=10,text ="WHILE", command = wloop).grid(row=11,column=1)
Tkinter.Button(top,height=1,width=10,text ="DO-WHILE", command = dwloop).grid(row=11,column=2)
Tkinter.Label(top,text="INPUT OUTPUT",font="bold").grid(row=12,column=0)
Tkinter.Button(top,height=1,width=10,text ="INPUT", command = inp).grid(row=12,column=1)
Tkinter.Button(top,height=1,width=10,text ="OUTPUT", command = oup).grid(row=12,column=2)

top.resizable(width=False, height=False)
top.geometry('{}x{}'.format(370,390))
top.mainloop()

