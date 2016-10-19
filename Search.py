# -*- coding: utf-8 -*-
import run
from Tkinter import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


root = Tk()
root.title("search")
root.geometry('600x600')

def search():
	result.delete(0.0, END)
	key = var.get().decode('utf-8')
	res = run.TF_IDF(key)
	for r in res:
		result.insert(END,'相关度:'+r[1]+'\n')
		result.insert(END,r[2])
		result.insert(END,r[3]+'\n\n')
var = StringVar()
keyword = Entry(root,textvariable=var)
bn = Button(root,text='get',command = search)
keyword.pack()
bn.pack()
result = Text(root)

result.pack()




root.mainloop()