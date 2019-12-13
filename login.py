import tkinter.messagebox
from tkinter import*
from tkinter import ttk
import nr

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Nursery management system')
        self.root.geometry('600x400+0+0')
        self.root.configure(background='white')
        title = Label(self.root,text='Nursery Management System',bd=15,font=('times new roman',30,'bold'),bg='dark green',fg='cornsilk')
        title.pack(side=TOP,fill=X)

        mainframe = Frame(self.root,bd=4,relief=RIDGE,bg='green')
        mainframe.place(x=10,y=100,width=580,height=380)

        # all variables
        self.user_var = StringVar()
        self.pass_var = StringVar()

        # attributes
        mid = Label(mainframe,text='User Name',bg='green',fg='white',font=('times new roman',20,'bold'))
        mid.grid(row=1,column=1,pady=20,padx=20,sticky='w')
        pid = Entry(mainframe,textvariable=self.user_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        pid.grid(row=1,column=2,pady=10,padx=20,sticky='w')

        m_name = Label(mainframe,text='Password',bg='green',fg='white',font=('times new roman',20,'bold'))
        m_name.grid(row=2,column=1,pady=10,padx=20,sticky='w')
        name = Entry(mainframe,show='*',textvariable=self.pass_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        name.grid(row=2,column=2,pady=10,padx=20,sticky='w')

        # Button frame
        btn_frame = Frame(mainframe,bd=4,relief=RIDGE,bg='green')
        btn_frame.place(x=220,y=160,width=100)
       
        add = Button(btn_frame,text='Log in',width=10,command=self.login).grid(row=0,column=0,padx=10,pady=10) 
    def login(self):
        if self.user_var.get()=='' or self.pass_var.get()=='':
            self.clear()
            messagebox.showerror('Error','Required field')
        elif self.user_var.get() =='nursery' or self.pass_var.get() == '123456':
            messagebox.showinfo('Successfully logged in')
            self.root.destroy()
            #x=nr.Nursery()
            
            
                
        
    def clear(self):
        self.user_var.set('')
        self.pass_var.set('')
        
        
root = Tk()
ob = Login(root)
root.resizable(width=False,height=False)
root.mainloop()
