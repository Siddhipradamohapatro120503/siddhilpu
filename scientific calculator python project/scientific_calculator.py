import tkinter.messagebox
from tkinter import *
import math


root= Tk()
root.title("Scientific Calculator")
root.configure(background='#3A3B3C')
root.geometry("900x590+20+20")
root.iconbitmap('E:\Python\Tkinter\c.ico')
root.resizable(width=False, height=False)
frame = Frame(root,background="#686A6C")
frame.grid(padx=120, pady=50)


##############################################################################################
# function

def click(value):
    ex = txtDisplay.get()
    answer=''

    try:
        try:
            if value=="Clear":
                txtDisplay.delete(0,END)

            elif value=="cos":
                answer=math.cos(math.radians(eval(ex)))

            elif value=="sin":
                answer=math.sin(math.radians(eval(ex)))

            elif value=="Tan":
                answer=math.tan(math.radians(eval(ex)))

            elif value=="asin":
                try:
                    if 1>=float(ex)>=-1: # the value must lie between -1 to 1
                        answer=math.asin(math.radians(eval(ex)))
                    else:
                        txtDisplay.delete(0, END)
                        txtDisplay.insert(0, "Invalid input")
                        return
                except ValueError:
                    pass

            elif value=="acos":
                try:
                    if 1 >= float(ex) >= -1:
                        answer = math.acos(math.radians(eval(ex)))
                    else:
                        txtDisplay.delete(0, END)
                        txtDisplay.insert(0, "Invalid input")
                        return
                except ValueError:
                    pass

            elif value=="atan":
                try:
                    if 1 >= float(ex) >= -1:
                        answer = math.atan(math.radians(eval(ex)))
                    else:
                        txtDisplay.delete(0, END)
                        txtDisplay.insert(0, "Invalid input")
                        return
                except ValueError:
                    pass

            elif value=='sqrt':
                answer=math.sqrt(eval(ex))

            elif value=='Log':
                try:
                    answer=math.log10(eval(ex))
                except ValueError:
                    pass

            elif value=='exp': # check the range of exp
                answer=math.exp(eval(ex))

            elif value=='INV':
                answer=ex[::-1]

            elif value=='Abs':
                answer=abs(eval(ex))

            elif value=='floor':
                answer=math.floor(eval(ex))

            elif value=='ceil':
                answer=math.ceil(eval(ex))


            elif value=='=':
                try:
                    answer=eval(ex)
                except ZeroDivisionError:
                    txtDisplay.delete(0,END)
                    txtDisplay.insert(0,"Invalid division")
                    return

            elif value=="pow":
                txtDisplay.insert(END,"**")
                return

            elif value=="Degree":
                answer=math.degrees(eval(ex))
                radiobutton1.config(background="#3A3B3C")
                radiobutton2.config(background="white")


            elif value=="Radians":
                answer=math.radians(eval(ex))
                radiobutton2.config(background="#3A3B3C")
                radiobutton1.config(background="white")


            else:
                txtDisplay.insert(END,value)
                return


            txtDisplay.delete(0,END)
            txtDisplay.insert(0,answer)

        except ZeroDivisionError:
            txtDisplay.delete(0, END)
            txtDisplay.insert(0, "Invalid division")
            return

    except SyntaxError:
        pass

###########################################################################3
# Entry Creation

txtDisplay = Entry(frame, font=('Helvetica', 20, 'bold'),
                    fg='white',background="gray",
                   bd=30, width=37, justify=LEFT)
txtDisplay.grid(row=0, column=0, columnspan=8, pady=1)
# txtDisplay.insert(0, "0") # to set a default value for the entry
##########################################################################
lable= Label(frame, text="INPUT VALUE IN", height=4, background="#686A6C",
             font="Arial,10").grid(row=3, column=0, columnspan=3)

radiobutton2= Radiobutton(frame, text="Radians", value="Radians",
                          command=lambda radiobutton2="Radians": click(radiobutton2))
radiobutton2.grid(row=3, column=5)

radiobutton1= Radiobutton(frame, text="Degree", value="Degree",background="#3A3B3C",
                          command=lambda radiobutton1="Degree": click(radiobutton1))
radiobutton1.grid(row=3, column=4)


#############################################################################################
#############################################################################################
# Buttons Creation

values=["INV","Log","(",")","Clear","+","sqrt","sin","cos","Tan","7","8","9","-","%","asin","acos","atan",
        "4","5","6","/","//","pow","exp","Abs","1","2","3","*","**","ceil","floor",",","0",".","="]

RowValue=4
ColumnValue=0
span=1
w=5
for i in values:
    color="gray"
    if RowValue==8 and ColumnValue==6:
        color="#2B3856"
    button1= Button(frame, text=i, font=5, bd=10, bg=color, fg="white", cursor="arrow", width=w, height=1,
                        activebackground="gray", command=lambda button1=i: click(button1))
    button1.grid(row=RowValue,column=ColumnValue,columnspan=span)
    ColumnValue+=1
    if span==2:
        ColumnValue += 1

    if ColumnValue==8:
        RowValue+=1
        ColumnValue=0

    if ColumnValue==4 and RowValue==4:
        span=2
        w=12
    elif ColumnValue==3 and RowValue==8:
        span=2
        w=12
    elif ColumnValue==6 and RowValue==8:
        span=2
        w=12
    else:
        span=1
        w=5

###############################################################################################
###############################################################################################
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator",
                                        "Do you want to exit ?")
    if iExit > 0:
        root.destroy()
        return



menubar = Menu(root)
lab = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calculator", menu=lab)
Exit = Menu(menubar, tearoff=0)
Exit.add_command(label="Exit", command=iExit)
menubar.add_cascade(label="Exit", menu=Exit)
root.config(menu=menubar)


root.mainloop()
