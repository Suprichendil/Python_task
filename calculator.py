##import tkinter as tk
from tkinter import *
app =Tk()
app.geometry("170x230")
app.title("Calculator")


ent = Entry(app, width=16, borderwidth=3, relief=RIDGE)
ent.grid(pady=10,row=0,sticky="w",padx=15)


def delete():
    a = ent.get()
    ent.delete(first=len(a) - 1, last="end")

def fresult():
    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0, "end")
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert("end", c_res)


def clearf():
    ent.delete(0, "end")

clean = Button(app,text="Clear",width=4,command=clearf,bg="blue",fg="white",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=125)
Num_nine = Button(text="9",width=3,command=lambda : ent.insert("end","9"),borderwidth=3,relief=RIDGE)
Num_nine.grid(row=1,sticky="w",padx=15)
Num_eight = Button(text="8",width=3,command=lambda : ent.insert("end","8"),borderwidth=3,relief=RIDGE)
Num_eight.grid(row=1,sticky="w",padx=45)
Num_seven = Button(app,text="7",width=3,command=lambda : ent.insert("end","7"),borderwidth=3,relief=RIDGE)
Num_seven.grid(row=1,sticky="w",padx=75)
Add_plus = Button(app,text="+",width=3,command=lambda : ent.insert("end","+"),borderwidth=3,relief=RIDGE)
Add_plus.grid(row=1,sticky="e",padx=125)
Num_six = Button(text="6",width=3,command=lambda : ent.insert("end","6"),borderwidth=3,relief=RIDGE)
Num_six.grid(row=2,sticky="w",padx=15,pady=5)
Num_five = Button(text="5",width=3,command=lambda : ent.insert("end","5"),borderwidth=3,relief=RIDGE)
Num_five.grid(row=2,sticky="w",padx=45,pady=5)
Num_four = Button(app,text="4",width=3,command=lambda : ent.insert("end","4"),borderwidth=3,relief=RIDGE)
Num_four.grid(row=2,sticky="w",padx=75,pady=5)
Sub_minus = Button(app,text="-",width=3,command=lambda : ent.insert("end","-"),borderwidth=3,relief=RIDGE)
Sub_minus.grid(row=2,sticky="e",padx=125,pady=5)
Num_three = Button(text="3",width=3,command=lambda : ent.insert("end","3"),borderwidth=3,relief=RIDGE)
Num_three.grid(row=3,sticky="w",padx=15,pady=5)
Num_two = Button(text="2",width=3,command=lambda : ent.insert("end","2"),borderwidth=3,relief=RIDGE)
Num_two.grid(row=3,sticky="w",padx=45,pady=5)
Num_one = Button(app,text="1",width=3,command=lambda : ent.insert("end","1"),borderwidth=3,relief=RIDGE)
Num_one.grid(row=3,sticky="w",padx=75,pady=5)
Mul_multiply = Button(app,text="",width=3,command=lambda : ent.insert("end",""),borderwidth=3,relief=RIDGE)
Mul_multiply.grid(row=3,sticky="e",padx=125,pady=5)
Num_zero = Button(text="0",width=3,command=lambda : ent.insert("end","0"),borderwidth=3,relief=RIDGE)
Num_zero.grid(row=4,sticky="w",padx=15,pady=5)
Num_double_zero = Button(text="00",width=3,command=lambda : ent.insert("end","00"),borderwidth=3,relief=RIDGE)
Num_double_zero.grid(row=4,sticky="w",padx=45,pady=5)
Button_dot = Button(app,text=".",width=3,command=lambda : ent.insert("end","."),borderwidth=3,relief=RIDGE)
Button_dot.grid(row=4,sticky="w",padx=75,pady=5)
Div_divide = Button(app,text="/",width=3,command=lambda : ent.insert("end","/"),borderwidth=3,relief=RIDGE)
Div_divide.grid(row=4,sticky="e",padx=125,pady=5)
result = Button(app,text="=",width=12,command=fresult,bg="white",fg="red",borderwidth=3,relief=RIDGE)
result.grid(row=5,sticky="w",padx=15,pady=5)
Char_modulus = Button(app,text="%",width=2,command=lambda : ent.insert("end","%"),borderwidth=3,relief=RIDGE)
Char_modulus.grid(row=5,sticky="e",padx=125,pady=5)
delete = Button(app,text="Del",width=3,command=delete,borderwidth=3,relief=RIDGE)
delete.grid(row=5,sticky="w",padx=80,pady=5)

app.mainloop()
##def add(number1,number2):
##        number3= number1+number2
##        return number3
##
##def sub(number1,number2):
##        number3= number1-number2
##        return number3
##
##def mul(number1,number2):
##        number3= number1*number2
##        return number3
##
##def div(number1,number2):
##        number3= number1/number2
##        return number3
##
##def allop(number1,number2):
##        Alloperation= (number1+number2,number1-number2,number1*number2,number1/number2)
##        return Alloperation
##
    
# print("---- Menu----")
# print("---- 1. Addition----")
# print("---- 2. Substraction----")
# print("---- 3. Multiplication----")
# print("---- 4. Division----")
# print("---- 5. All Operation----")
# print("---- 6. Exit----")   

##def menus():
##    print("---- Menu----")
##    print("---- 1. Addition----")
##    print("---- 2. Substraction----")
##    print("---- 3. Multiplication----")
##    print("---- 4. Division----")
##    print("---- 5. All Operation----")
##    print("---- 6. Exit----")  

## Main
##menus()
##choice = int(input("Enter your number:-  "))
##
##while choice<7:
##        if choice==6:
##            print("------You are exit------")
##                menus()
##                break
##
##        else:
##                number1 = int(input("Enter your first number :- "))
##                number2 = int(input("Enter your second number:- "))
##                if choice==1:
##                        print("Addition:- ", add(number1,number2))
##                elif choice==2:
##                        print("Substraction:- ", sub(number1,number2))
##                elif choice==3:
##                        print("Multiplication:- ", mul(number1,number2))
##                elif choice==4:
##                        print("Division:- ", div(number1,number2))
##
##                elif choice==5:
##                        print("All Operation:- ", allop(number1,number2))
##                menus()
##                break
