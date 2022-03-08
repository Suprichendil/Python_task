from tkinter import *
##import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var=IntVar()
Age=IntVar()
Batch=IntVar()

def details():
    name=Fullname.get()
    email=Email.get()
    age=Age.get()
    gender=var.get()
    department=var.get()
    batch=Batch.get()


    a=open("Candidate_details.txt","w")
    a.write("Candidate Name:")
    a.write(str(name))
    a.write("\nCandidate Email:")
    a.write(str(email))
    a.write("\nCandidate age:")
    a.write(str(age))
    a.write("\nCandidate gender:")
    a.write(str(gender))
    a.write("\nDepartment:")
    a.write(str(department))
    a.write("\nBatch:")
    a.write(str(batch))
    a.close()
    



##def database():
##   name1=Fullname.get()
##   email=Email.get()
##   gender=var.get()
##   country=c.get()
##   prog=var1.get()
##   conn = sqlite3.connect('Form.db')
##   with conn:
##      cursor=conn.cursor()
##   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
##   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
##   conn.commit()
##   
   
             
label_0 = Label(root, text="CANDIDATE DETAILS",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=80,y=230)

Radiobutton(root, text="Male",padx = 1, variable=var, value=1).place(x=230,y=230)
Radiobutton(root, text="Female",padx = 10, variable=var, value=2).place(x=280,y=230)

label_4 = Label(root, text="Age",width=20,font=("bold", 10))
label_4.place(x=80,y=280)

entry_4 = Entry(root,textvar=Age)
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Department",width=20,font=("bold", 10))
label_5.place(x=80,y=310)

Radiobutton(root, text="CSE",padx = 1, variable=var, value=1).place(x=240,y=310)
Radiobutton(root, text="ECE",padx = 10, variable=var, value=2).place(x=310,y=310)
Radiobutton(root, text="MECH",padx = 20, variable=var, value=3).place(x=380,y=310)

label_6 = Label(root, text="Batch",width=20,font=("bold", 10))
label_6.place(x=80,y=350)

entry_6 = Entry(root,textvar=Batch)
entry_6.place(x=240,y=350)

Button(root, text='Submit',width=20,bg='blue',fg='white',command=details).place(x=150,y=400)

root.mainloop()
print("Your form is successfully submitted!")
