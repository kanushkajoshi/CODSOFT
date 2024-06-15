import tkinter
from tkinter import *

root = Tk()
root.title("CALCULATOR")   # the string name to my app
root.geometry("570x600+100+200")   # dimension to the frame
root.resizable(False, False)
root.configure(bg="#282C34")  # Change background color

equation = ""
# define later after we create buttons
def show(value):         
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

label_result = Label(root, width=25, height=2, text="", font=("arial", 30), bg="#ABB2BF", fg="#282C34")
label_result.pack()

# first we will be creating buttons for calculator
button_color = "#61AFEF"  # Default button color
operator_color = "#C678DD"  # Color for operator buttons
equal_color = "#98C379"  # Color for the equal button

Button(root, text="C", width=5, height=1, font=("italic arial", 35, "bold"), bd=1, fg="#000000", bg="#E06C75", command=lambda: clear()).place(x=10, y=100)
Button(root
