from tkinter import *

root=Tk()
'''leftframe=Frame(root)
leftframe.pack(side=TOP)# and TOP)
rightframe=Frame(root)
rightframe.pack(side=TOP)
centerframe=Frame(root)
centerframe.pack(side=BOTTOM)
'''
Label1=Label(root,text="CPU",fg="grey")
Label1.grid(row=0,column=1, columnspan=3)
Label2=Label(root,text="Player",fg="red")
Label2.grid(row=0,column=6)#, columnspan=3)
Button1=Button(root,text="Start",fg="green")
Button1.grid(row=1,column=2)


root.mainloop()



