from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
import shutil
import json

orgdir="C:/program files"
directory = "c:/program files/boogeymanwallet"
checker= os.listdir(orgdir)

try:
 if ['boogeymanwallet'] in checker:
   pass
 else :
    os.mkdir(directory)
    
except FileExistsError:
  pass


window=Tk()
window.resizable(False,False)
window.title("YOUR PERSONAL WALLET APP : by @boogeyman on github")

iconphoto=PhotoImage(file="bank.png")
labelphoto=PhotoImage(file="bank1.png")
window.iconphoto(FALSE,iconphoto)
WIDTH=600
HEIGHT=450
x = int((window.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((window.winfo_screenheight() / 2) - (HEIGHT / 2 +50))
window.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
label1=Label(image=labelphoto)
label1.place(width=400,height=450,x=0,y=0)

#functions
def loadbutton():
   messagebox.showwarning(title="please choose a valid file",message="PLEASE ENTER A FILE THAT HES BEEN CREATED THROUGH THIS WALLET \n I AM NOT RESPONSIBLE FOR ANY OTHER JSON FILES THAT YOU LOAD INTO MY PROGRAM")
   selected=filedialog.askopenfilename(initialdir="c:\\program files",title="Choose A File To Import",
                                        filetypes=[("Json files","*.json")])
   try:
      shutil.move(selected,directory)
      messagebox.showinfo(message="SUCCESS !!!!!!!!!!")
   except shutil.Error:
      messagebox.showerror(message="file already exists..\n try changing name")

def searbutton():
   searchquery=searchvar.get()+".json"
   checker1=os.listdir(directory)
   try:
      if searchquery not in checker1 :
         messagebox.showerror(title="404 :(",message="not found unfortunatly") 
      else:
        messagebox.showinfo(title="SUCCESS!!",message="IT EXISTS!!!!")
   except FileExistsError + FileNotFoundError:
      pass      

def search_tran():
  global searchvar
  global searchentry
  searchvar=StringVar()
  searchwindow=Toplevel(window)
  searchwindow.resizable(False,False)
  WIDTH2=300
  HEIGHT2=150
  x = int((searchwindow.winfo_screenwidth() / 2) - (WIDTH2 / 2))
  y = int((searchwindow.winfo_screenheight() / 2) - (HEIGHT2 / 2 +100))
  searchwindow.geometry(f'{WIDTH2}x{HEIGHT2}+{x}+{y}')
  searchlabel=Label(searchwindow, text="SEARCH A TRANSACTION",
         font=('Calibri',12,"bold"))
  searchlabel.pack(anchor=N)
  searchentry=Entry(searchwindow,textvariable=searchvar,bg="#26e11e",width=30)
  searchentry.pack(side="top")
  notifiylabel=Label(searchwindow,text="**NOTE:PLEASE RESPECT THE CARACTER ORDER \n BECAUSE ELSE IT WOULDNT WORK **",
         font=('Calibri',10,"bold"))
  notifiylabel.pack(side="top")
  searchbutton=Button(searchwindow,text="SEARCH",
                      font=('calibri',10,"bold"),width=20,height=10,
                      relief="groove",fg="#cab697",bg="#68756b",command=searbutton)
  searchbutton.pack(side="top",pady=10)




def disp_tran():
    filepath1=filedialog.askopenfilename(initialdir="c:\\program files\\boogeymanwallet",
                                        title="choose a file to display",
                                        filetypes=[("Json files","*.json")])
    try:
       tran_file =open(filepath1,"r")
       tran_file_data=json.load(tran_file)
       messagebox.showinfo(title="your info",message=str([tran_file_data]))
    except FileNotFoundError:
       pass   
    


def remo_tran():
    filepath=filedialog.askopenfilename(initialdir="c:\\program files\\boogeymanwallet",
                                        title="choose a file to delete",
                                        filetypes=[("Json files","*.json")])
    print(filepath)
    try:
       os.remove(filepath)
       messagebox.showinfo(title="Succes!",message="Transaction Deleted Succesfully")
    except FileNotFoundError:
       pass


def adding_tranbutton():
  tran_title = t_tran_name.get()
  amount = t_amount.get()
  types = t_type_oftran.get()
  note = t_note.get()
  all_transactions = os.listdir(directory)

  if tran_title == "" or amount == "" or types == "" or note == "":
        messagebox.showerror(title="Type Error",message="All Fields Required")
        return
  
  for tran_check in all_transactions:
         if tran_title+".json" == tran_check:
            messagebox.showerror(title="File Error",message="Already Exists")
            return
  else:
            data=[{"Expense  ":tran_title,"Amount  ":amount,"Type  ":types,"Note  ":note,}]
            with open("c:/program files/boogeymanwallet/"+tran_title+".json","w") as file:
             json.dump(data,file)
            messagebox.showinfo(title="Succes!",message="Added Succesfully")



def adding_tran():
  #variables
  global t_tran_name
  global t_amount
  global t_type_oftran
  global t_note
  t_tran_name=StringVar()
  t_amount=StringVar()
  t_type_oftran=StringVar()
  t_note=StringVar()
  #screen
  add_window=Toplevel(window)
  add_window.title("Add A Transaction Please Sir !")
  add_window.resizable(False,False)
  WIDTH1=400
  HEIGHT1=200
  x = int((add_window.winfo_screenwidth() / 2) - (WIDTH1 / 2))
  y = int((add_window.winfo_screenheight() / 2) - (HEIGHT1 / 2 +100))
  add_window.geometry(f'{WIDTH1}x{HEIGHT1}+{x}+{y}')


  #Labels
  Label(add_window, text="Please Enter Your Details Below To Save The Transaction : ",
         font=('Calibri',12)).grid(row=0,sticky=N,pady=10)
  Label(add_window, text="Title :", font=('Calibri',12)).grid(row=1,sticky=W)
  Label(add_window, text="Amount :", font=('Calibri',12)).grid(row=2,sticky=W)
  Label(add_window, text="Type :", font=('Calibri',12)).grid(row=3,sticky=W)
  Label(add_window, text="Note :", font=('Calibri',12)).grid(row=4,sticky=W)


  #Entries
  Entry(add_window,textvariable=t_tran_name).grid(row=1,column=0)
  Entry(add_window,textvariable=t_amount).grid(row=2,column=0)
  Entry(add_window,textvariable=t_type_oftran).grid(row=3,column=0)
  Entry(add_window,textvariable=t_note).grid(row=4,column=0)
  

  #Buttons
  Button(add_window, text="Add The Transaction",
          font=('Calibri',12),fg="#cab697",bg="#68756b",relief="groove",borderwidth=5,
          command=adding_tranbutton).grid(row=5,sticky=N,pady=10)





#Buttons
add_btn=Button(window,text="Add \n A \n Transaction",font=("SansSerif",12,"bold"),
               width=19,height=4,fg="#cab697",bg="#68756b",relief="solid",command=adding_tran)
add_btn.pack(anchor=E)


rem_btn=Button(window,text="Remove \n A \nTransaction",font=("SansSerif",12,"bold"),
               width=19,height=4,fg="#cab697",bg="#68756b",relief="solid",command=remo_tran)
rem_btn.pack(anchor=E)

disp_btn=Button(window,text="Display \n A \n Transaction",font=("SansSerif",12,"bold"),
               width=19,height=4,fg="#cab697",bg="#68756b",relief="solid",command=disp_tran)
disp_btn.pack(anchor=E)


srch_btn=Button(window,text="Search\n A \n Transaction",font=("SansSerif",12,"bold"),
               width=19,height=4,fg="#cab697",bg="#68756b",relief="solid",command=search_tran)
srch_btn.pack(anchor=E)

load_btn=Button(window,text="load\n An External\n Transaction",
                font=("SansSerif",12,"bold"),
               width=19,height=4,bg="#68756b",fg="#cab697",relief="solid",command=loadbutton)
load_btn.pack(anchor=E)

labimg=Label(window,image=iconphoto,height=20,width=95)
labimg.pack(anchor=W)


window.mainloop()


