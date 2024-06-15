#using module tkinter
import tkinter
from tkinter import *

root=Tk()
root.title("CUTE CALCi")   #the string name to my app
root.geometry("570x600+100+200")   #dimension to the frame
root.resizable(False,False)
root.configure(bg="#FF1493")

equation=""
#define later after we create buttons
def show(value):         
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)

label_result=Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()
#first we will be creating buttons for calculator
Button(root,text="C",width=5,height=1,font=("italic arial",35,"bold"),bd=1,fg="#000000",bg="#FFB6C1",command=lambda: clear()).place(x=10,y=100)
Button(root,text="%",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FADADD",command=lambda: show("%")).place(x=150,y=100)
Button(root,text="*",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FADADD",command=lambda: show("*")).place(x=290,y=100)
Button(root,text="/",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FADADD",command=lambda: show("/")).place(x=430,y=100)

Button(root,text="1",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("1")).place(x=10,y=200)
Button(root,text="2",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("2")).place(x=150,y=200)
Button(root,text="3",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("3")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FADADD",command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FADADD",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="7",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("7")).place(x=10,y=400)
Button(root,text="8",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("8")).place(x=150,y=400)
Button(root,text="9",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("9")).place(x=290,y=400)

Button(root,text="0",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("0")).place(x=10,y=500)
Button(root,text="00",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FF91A4",command=lambda: show("00")).place(x=150,y=500)
Button(root,text=".",width=5,height=1,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#FADADD",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("arial",35,"bold"),bd=1,fg="#000000",bg="#DC143C",command=lambda: calculate()).place(x=430,y=400)

root.mainloop()