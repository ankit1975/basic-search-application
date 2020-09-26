from tkinter import *
import wikipedia
root=Tk()
topf=Frame(root,width=400,height=100)
entry=Entry(topf)
entry.pack()
def call():
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
bottomf=Frame(root,width=400,height=200)
text=Text(bottomf,width=50,height=10,wrap=WORD)
scroll=Scrollbar(bottomf,command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
text.pack()
bottomf.pack()
root.mainloop()



