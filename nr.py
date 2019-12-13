import tkinter.messagebox
from tkinter import*
from tkinter import ttk
import pymysql
import login
class Nursery:
    def __init__(self,root):
        self.root = root
        self.root.title('Nursery management system')
        self.root.geometry('1300x700+0+0')
        self.root.configure(background='white')
        title = Label(self.root,text='Nursery Management System',bd=10,font=('times new roman',40,'bold'),bg='dark green',fg='cornsilk')
        title.pack(side=TOP,fill=X)

        mainframe = Frame(self.root,bd=4,relief=RIDGE,bg='green')
        mainframe.place(x=10,y=100,width=450,height=560)

        # all variables
        self.id_var = StringVar()
        self.name_var = StringVar()
        self.sname_var = StringVar()
        self.price_var = StringVar()
        self.qt_var = StringVar()
        self.shade_var = StringVar()

        m_title = Label(mainframe,text='Manage Plants',bg='green',fg='white',font=('times new roman',30,'bold'))
        m_title.grid(row=0,columnspan=2,pady=20)

        # attributes
        mid = Label(mainframe,text='PID No.',bg='green',fg='white',font=('times new roman',20,'bold'))
        mid.grid(row=1,column=0,pady=10,padx=20,sticky='w')
        pid = Entry(mainframe,textvariable=self.id_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        pid.grid(row=1,column=1,pady=10,padx=20,sticky='w')

        m_name = Label(mainframe,text='Name',bg='green',fg='white',font=('times new roman',20,'bold'))
        m_name.grid(row=2,column=0,pady=10,padx=20,sticky='w')
        name = Entry(mainframe,textvariable=self.name_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        name.grid(row=2,column=1,pady=10,padx=20,sticky='w')

        s_name = Label(mainframe,text='S. Name',bg='green',fg='white',font=('times new roman',20,'bold'))
        s_name.grid(row=3,column=0,pady=10,padx=20,sticky='w')
        sname = Entry(mainframe,textvariable=self.sname_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        sname.grid(row=3,column=1,pady=10,padx=20,sticky='w')

        price = Label(mainframe,text='Price',bg='green',fg='white',font=('times new roman',20,'bold'))
        price.grid(row=4,column=0,pady=10,padx=20,sticky='w')
        mprice = Entry(mainframe,textvariable=self.price_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        mprice.grid(row=4,column=1,pady=10,padx=20,sticky='w')

        qt = Label(mainframe,text='Quantity',bg='green',fg='white',font=('times new roman',20,'bold'))
        qt.grid(row=5,column=0,pady=10,padx=20,sticky='w')
        quantity = Entry(mainframe,textvariable=self.qt_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        quantity.grid(row=5,column=1,pady=10,padx=20,sticky='w')

        shade = Label(mainframe,text='Shade No.',bg='green',fg='white',font=('times new roman',20,'bold'))
        shade.grid(row=6,column=0,pady=10,padx=20,sticky='w')
        mshade = Entry(mainframe,textvariable=self.shade_var,font=('times new roman',15,'bold'),bd=5,relief=GROOVE)
        mshade.grid(row=6,column=1,pady=10,padx=20,sticky='w')

        # Button frame
        btn_frame = Frame(mainframe,bd=4,relief=RIDGE,bg='green')
        btn_frame.place(x=10,y=500,width=430)
        
        add = Button(btn_frame,text='Add',width=8,command=self.add_plants).grid(row=0,column=0,padx=5,pady=5)
        update = Button(btn_frame,text='Update',width=8,command=self.update).grid(row=0,column=1,padx=10,pady=10)
        delete = Button(btn_frame,text='Delete',width=8,command=self.delete).grid(row=0,column=2,padx=10,pady=10)
        clear = Button(btn_frame,text='Clear',width=8,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        clear2 = Button(btn_frame,text='Log out',width=8,command=self.out).grid(row=0,column=4,padx=10,pady=10)

        #details frame
        detailframe = Frame(self.root,bd=4,relief=RIDGE,bg='green')
        detailframe.place(x=480,y=100,width=800,height=560)
        
        m_title = Label(detailframe,text='Show Plants Details',bg='green',fg='white',font=('times new roman',30,'bold'))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        #table frame
        table = Frame(detailframe,bd=4,relief=RIDGE,bg='green')
        table.place(x=10,y=80,width=760,height=470)

        # show details
        scroll_x=Scrollbar(table,orient=HORIZONTAL)
        scroll_y=Scrollbar(table,orient=VERTICAL)
        self.plant = ttk.Treeview(table,columns=('pid','name','sname','price','qt','shade'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command = self.plant.xview)
        scroll_y.config(command = self.plant.yview)
        self.plant.heading('pid',text='PID')
        self.plant.heading('name',text='Name')
        self.plant.heading('sname',text='Scientific Name')
        self.plant.heading('price',text='Price')
        self.plant.heading('qt',text='Quantity')
        self.plant.heading('shade',text='Shade')
        self.plant['show']='headings'
        self.plant.column('pid',width=100)
        self.plant.column('name',width=100)
        self.plant.column('sname',width=100)
        self.plant.column('price',width=100)
        self.plant.column('qt',width=100)
        self.plant.column('shade',width=100)
        self.plant.pack(fill=BOTH,expand=1)
        self.plant.bind('<ButtonRelease-1>',self.get_cursor)

        self.fetch_all()

    
    def add_plants(self):
        if self.id_var.get()=='' or self.name_var.get()=='' or self.price_var.get()=='' or self.qt_var.get()=='' or self.shade_var.get()=='':
            messagebox.showerror('Error','Required field')
        else:
            con = pymysql.connect(host='localhost',user='root',password='',database='plant')
            cur = con.cursor()
            cur.execute('insert into addplant values(%s,%s,%s,%s,%s,%s)',(self.id_var.get(),
                                                                            self.name_var.get(),
                                                                            self.sname_var.get(),
                                                                            self.price_var.get(),
                                                                            self.qt_var.get(),
                                                                            self.shade_var.get())
                                                                                            )
            con.commit()
            self.fetch_all()
            self.clear()
            con.close()
            messagebox.showinfo('Successfully! Inserted info')

    def fetch_all(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='plant')
        cur = con.cursor()
            #plant.delete(0,END)
        cur.execute('select * from addplant')
        rows = cur.fetchall()
            
        if len(rows) != 0:
            self.plant.delete(*self.plant.get_children())
            for row in rows:
                self.plant.insert('',END,values=row)
                 
                con.commit()
                print(row)
        con.close()

    def clear(self):
        self.id_var.set('')
        self.name_var.set('')
        self.sname_var.set('')
        self.price_var.set('')
        self.qt_var.set('')
        self.shade_var.set('')

    def get_cursor(self,ev):
        cursor_row = self.plant.focus()
        contents = self.plant.item(cursor_row)
        row = contents['values']
        self.id_var.set(row[0])
        self.name_var.set(row[1])
        self.sname_var.set(row[2])
        self.price_var.set(row[3])
        self.qt_var.set(row[4])
        self.shade_var.set(row[5])

    def update(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='plant')
        cur = con.cursor()
        cur.execute('update addplant set mname=%s,sname=%s,price=%s,qt=%s,shade=%s where pid=%s',(
                                                                        self.name_var.get(),
                                                                        self.sname_var.get(),
                                                                        self.price_var.get(),
                                                                        self.qt_var.get(),
                                                                        self.shade_var.get(),
                                                                        self.id_var.get())
                                                                                        )
        con.commit()
        self.fetch_all()
        self.clear()
        con.close()
    def delete(self):
        con = pymysql.connect(host='localhost',user='root',password='',database='plant')
        cur = con.cursor()
        cur.execute('delete from addplant where pid=%s',self.id_var.get())
        con.commit()
        con.close()
        self.fetch_all()
        self.clear()

    def out(self):
        self.root.destroy()
        x=login.login()
        
        #return None
root = Tk()
ob = Nursery(root)
root.resizable(width=False,height=False)
root.mainloop()
