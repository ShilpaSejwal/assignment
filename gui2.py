# question 1
'''
from tkinter import*
root = Tk()
dictt={}
root.title('list')
root.geometry('250x250')
dictt = {'shilpa' : 7836986818,
        'arti' : 9555937083,
        'rithvik' : 9953466755,
        'chandan' : 9999878223,
        'mahi': 9999284980,
        'deepanshu': 9818857805}

frame1=Frame(root)
frame1.pack()

s = Scrollbar(frame1)
s.pack(side=RIGHT,fill=Y)
listL = Listbox(frame1,yscrollcommand=s.set)

for x in dictt:
 
    listL.insert(END,x)
   

listL.pack(side=LEFT,fill=X)
s.config(command = listL.yview)

root.mainloop()
'''

# question 2


from tkinter import*
root = Tk()
dictt={}
root.title('list')
root.geometry('250x250')
dictt = {'shilpa' : 7836986818,
        'arti' : 9555937083,
        'rithvik' : 9953466755,
        'chandan' : 9999878223,
        'mahi': 9999284980,
        'deepanshu': 9818857805}

frame1=Frame(root)
frame1.pack()

s = Scrollbar(frame1)
s.pack(side=RIGHT,fill=Y)
listL = Listbox(frame1,yscrollcommand=s.set)

for x in dictt:
 
    listL.insert(END,x)
   

listL.pack(side=LEFT,fill=X)
s.config(command = listL.yview)
def onclick():
    dictt[e1.get()]=e2.get()
    listL.insert(END,e1.get())

frame2 = Frame(root)
frame2.pack()

lbL1 = Label(frame2,text="name")
lbL1.grid(row=0,column=0)

lbL2 = Label(frame2,text="mobile number")
lbL2.grid(row=1,column=0)

e1 = Entry(frame2)
e1.grid(row=0,column=1)

e2 = Entry(frame2)
e2.grid(row=1,column=1)

textB = Button(frame2,text='add it',bg='red', command=onclick)
textB.grid(row=2,column=1)

root.mainloop()
