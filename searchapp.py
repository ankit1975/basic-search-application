from tkinter import *
from tkinter.font import Font
import wikipedia
root=Tk()
root.geometry("600x600+50+50")
topf=Frame(root,width=100,height=300)
entry=Entry(topf,background="black",foreground="white",width=50)
entry.pack()
def call():
    button.config(background="green")
    entryvalue=entry.get()
    text.delete(1.0,END)
    try:
        answervalue=wikipedia.summary(entryvalue)
        text.insert(INSERT,answervalue)
    except:
        text.insert(INSERT,"please check input or internet connecton")
button=Button(topf,text="search",command=call)
button.pack()
topf.pack(side=TOP)
bottomf=Frame(root,width=250,height=500)
f=Font(family="Times New Roman",size=15)
text=Text(bottomf,wrap=WORD,font=f)
scroll=Scrollbar(bottomf,command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
text.pack()
bottomf.pack()
root.mainloop()



