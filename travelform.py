from tkinter import *
root=Tk()
root.geometry("450x400")
root.maxsize(450,400)
def getvals():
    if (foodservicevar.get()==1):
        print(namevar.get(),"you got your meal in sometime")
    else:
        print(namevar.get(),"you didn't get meal")
    f=open("repo.txt","a")
    f.write(f"{namevar.get(),phonevar.get(),paymentmodevar.get()}\n")
    f.close()
root.title("travel form")
Label(root,text="Welcome to my travel",font="comicansms 14 bold",pady=14).grid(row=0,column=2)
name=Label(root,text="Name :-").grid(row=1,column=0)
phone=Label(root,text="Phone No :-").grid(row=2,column=0)
gender=Label(root,text="Gender :-").grid(row=3,column=0)
emergencycontact=Label(root,text="Emergency Contact :-").grid(row=4,column=0)
paymentmode=Label(root,text="Payment Mode :-").grid(row=5,column=0)

#create variable for storing value
namevar=StringVar()
phonevar=StringVar()
gendervar=StringVar()
emergencycontactvar=StringVar()
paymentmodevar=StringVar()
foodservicevar=IntVar()

#using event class for taking value
Entry(root,textvariable=namevar).grid(row=1,column=2)
Entry(root,textvariable=phonevar).grid(row=2,column=2)
Entry(root,textvariable=gendervar).grid(row=3,column=2)
Entry(root,textvariable=emergencycontactvar).grid(row=4,column=2)
Entry(root,textvariable=paymentmodevar).grid(row=5,column=2)

#checkbox
foodservice = Checkbutton(root,text="would you take meal",variable=foodservicevar,pady=5)
foodservice.grid(row=6,column=2)

#button and command
Button(text="Submit to my travel",command=getvals,fg="red").grid(row=7,column=2)
root.mainloop()
