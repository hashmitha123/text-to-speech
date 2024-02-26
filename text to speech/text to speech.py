import tkinter as tk
from tkinter import*
import pyttsx3

engine=pyttsx3.init()
def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

t=Tk()

textv=StringVar()
b=LabelFrame(t,text="text to speech",font=20,bd=2)
b.pack(fill="both",expand="yes",padx=10,pady=10)
c=Label(b,text="text",font=30)
c.pack(side=tk.LEFT,padx=5)
text=Entry(b,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)
btn=Button(b,text="speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)
t.title("text to speech")
t.geometry("500x500")
t.resizable(False,False)
t.mainloop()


