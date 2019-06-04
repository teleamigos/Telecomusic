
from tkinter import *

root=Tk()
root.title("Telecomusic")
root.configure(background="pale goldenrod")
Text_Entry=Entry(root)
Text_Entry.pack()
Text_Entry.focus_set()
def DownloadButton():
    print(Text_Entry.get())

Dbutton=Button(root,text="Download",width=10,command=DownloadButton)
Dbutton.pack()

root.mainloop()
