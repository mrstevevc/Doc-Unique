'''
Author: Stephen Lester
Last updated: September 30th, 2016
'''

from tkinter import *
from tkinter.filedialog import askopenfilename
from wordcounter import wordcounter

filename = ['']
words = ['','']

box = Tk()
box.configure()
box.geometry("450x225+50+50")
box.resizable(width=False, height=False)
box.title("Word Counter")

menu_bar = Menu(box)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=box.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)
box.config(menu=menu_bar)

entry_one = Entry(box, fg='black')
entry_one.config(font=('arial', 12))
entry_one.pack()
entry_one.place(x=300, y=50)

button_select = Button(text='Select file',  fg='black',
					 command=lambda: getfile())
button_select.config(font=('arial', 12))
button_select.pack()
button_select.place(x=10, y=50)

button_run = Button(text='Run', fg='black', command=lambda: click_run())  
button_run.config(font=('arial', 12))
button_run.pack()
button_run.place(x=185, y=150)

def click_run():
	wordcounter(filename[0], words)
	window = Toplevel()
	label_top = Label(window, text=words[0], height=0, width=100)
	label_top.pack()
	label_bottom = Label(window, text=words[1], height=0, width=100)
	label_bottom.pack()

def getfile():
	filename[0] = askopenfilename()
	entry_one.delete(0, END)
	entry_one.insert(0, filename[0])

box.mainloop()
