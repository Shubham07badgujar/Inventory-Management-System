from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import sqlite3

class memberClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg = "white")
        self.root.focus_force()
        #============================================
        #All variables =====
        self.var_mem_searchby = StringVar()
        self.var_mem_searchtxt = StringVar()

        self.var_mem_prn = StringVar()
        self.var_mem_gender = StringVar()
        self.var_mem_contact = StringVar()
        self.var_mem_name = StringVar()
        self.var_mem_dob = StringVar()
        self.var_mem_email = StringVar()
        self.var_mem_pass = StringVar()
        self.var_mem_usertype = StringVar()

        #==== Seaarch Frame ====
        SearchFrame = LabelFrame(self.root,text="Search Member",font=("goudy old style",12,"bold"),bd=2,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        #==== Options ====
        cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_mem_searchby,values=("Select","Email","Name","PRN"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_search.place(x=10,y=10,width=100)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_mem_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search = Button(SearchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=8,width=150,height=30)

        #===== Title =====
        title = Label(self.root,text="Member Details",font=("goudy old style",15),bg="#0f4d7d",fg="white",).place(x=50,y=100,width=1000)

        #====== Content =====
        #===== Row 1 =====
        lbl_memid = Label(self.root,text="Member ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_gender = Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_contact = Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_memid = Entry(self.root,textvariable=self.var_mem_prn,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=100)
        cmb_gender = ttk.Combobox(self.root,textvariable=self.var_mem_gender,values=("Select","Male","Female","Other"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_gender.place(x=500,y=150,width=100)
        cmb_gender.current(0)
        txt_contact = Entry(self.root,textvariable=self.var_mem_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=100)

        #===== Row 2 =====
        lbl_name = Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
        lbl_dob = Label(self.root,text="Date Of Birth",font=("goudy old style",15),bg="white").place(x=350,y=190)
        lbl_email = Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=750,y=190)

        txt_name = Entry(self.root,textvariable=self.var_mem_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
        txt_dob = Entry(self.root,textvariable=self.var_mem_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
        txt_email = Entry(self.root,textvariable=self.var_mem_email,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

        #===== Row 2 =====
        lbl_password = Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=50,y=230)
        lbl_utype = Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=350,y=230)

        txt_pass = Entry(self.root,textvariable=self.var_mem_pass,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
        cmb_utype = ttk.Combobox(self.root,textvariable=self.var_mem_usertype,values=("Admin","Member"),state="readonly",justify=CENTER,font=("gaudy old style",15))
        cmb_utype.place(x=500,y=230,width=180)
        cmb_utype.current(0)


        #==== Buttons =====
        btn_add = Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update = Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_delete = Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#f44336",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="#607d8b",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=28)


        #==== Member Details =====

        mem_frame = Frame(self.root,bd=3,relief=RIDGE)
        mem_frame.place(x=0,y=350,relwidth=1,height=150)

        scrolly = Scrollbar(mem_frame,orient=VERTICAL)
        scrollx = Scrollbar(mem_frame,orient=HORIZONTAL)

        self.MemberTable=ttk.Treeview(mem_frame,columns=("memid","name","email","gender","contact","dob","pass","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.MemberTable.xview)
        scrolly.config(command=self.MemberTable.yview)
        self.MemberTable.heading("memid",text="Member ID")
        self.MemberTable.heading("name",text="Name")
        self.MemberTable.heading("email",text="Email")
        self.MemberTable.heading("gender",text="Gender")
        self.MemberTable.heading("contact",text="Contact")
        self.MemberTable.heading("dob",text="DOB")
        self.MemberTable.heading("pass",text="Password")
        self.MemberTable.heading("utype",text="User Type")

        self.MemberTable["show"]="headings"

        self.MemberTable.column("memid",width=90)
        self.MemberTable.column("name",width=100)
        self.MemberTable.column("email",width=100)
        self.MemberTable.column("gender",width=100)
        self.MemberTable.column("contact",width=100)
        self.MemberTable.column("dob",width=100)
        self.MemberTable.column("pass",width=100)
        self.MemberTable.column("utype",width=100)
        self.MemberTable.pack(fill=BOTH,expand=1)
        self.MemberTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#=====================================================================

    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_mem_prn.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_mem_prn.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error", "This Member ID already assigned , try different",parent=self.root)
                else:
                    cur.execute("Insert into member (memid,name,email,gender,contact,dob,pass,utype) values(?,?,?,?,?,?,?,?)",(
                        self.var_mem_prn.get(),
                        self.var_mem_name.get(),
                        self.var_mem_email.get(),
                        self.var_mem_gender.get(),
                        self.var_mem_contact.get(),
                        self.var_mem_dob.get(),
                        self.var_mem_pass.get(),
                        self.var_mem_usertype.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Member Added Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            
 
    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from member")
            rows=cur.fetchall()
            self.MemberTable.delete(*self.MemberTable.get_children())
            for row in rows:
                self.MemberTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def get_data(self,ev):
        f=self.MemberTable.focus()
        content=(self.MemberTable.item(f))
        row=content['values']
        # print(row)
        self.var_mem_prn.set(row[0])
        self.var_mem_name.set(row[1])
        self.var_mem_email.set(row[2])
        self.var_mem_gender.set(row[3])
        self.var_mem_contact.set(row[4])
        self.var_mem_dob.set(row[5])
        self.var_mem_pass.set(row[6])
        self.var_mem_usertype.set(row[7])


#======== UPDATE DATA =======================================================================================

    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_mem_prn.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_mem_prn.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Member ID",parent=self.root)
                else:
                    cur.execute("Update member set name=?,email=?,gender=?,contact=?,dob=?,pass=?,utype=? where memid=?",(
                
                        self.var_mem_name.get(),
                        self.var_mem_email.get(),
                        self.var_mem_gender.get(),
                        self.var_mem_contact.get(),
                        self.var_mem_dob.get(),
                        self.var_mem_pass.get(),
                        self.var_mem_usertype.get(),
                        self.var_mem_prn.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Member Updated Successfully",parent=self.root)
                    self.show()

                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
#============ DELETE Button =========================================================================

    def delete(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_mem_prn.get()=="":
                messagebox.showerror("Error","Member ID Must be required",parent=self.root)
            else:
                cur.execute("SELECT * FROM member WHERE memid=?",(self.var_mem_prn.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Member ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete ?",parent=self.root)
                    if op == True:
                        cur.execute("delete from member where memid=? ",(self.var_mem_prn.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Member Deleted Successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#======= Clear Button ================================================================================================

    def clear(self):
        self.var_mem_prn.set("")
        self.var_mem_name.set("")
        self.var_mem_email.set("")
        self.var_mem_gender.set("Select")
        self.var_mem_contact.set("")
        self.var_mem_dob.set("")
        self.var_mem_pass.set("")
        self.var_mem_usertype.set("Admin")
        self.var_mem_searchtxt.set("")
        self.var_mem_searchby.set("Select")

        self.show()

#======= Search Button ===============================
    def search(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            if self.var_mem_searchby.get()=="Select":
                messagebox.showerror("Erro","Select Search By Option",parent=self.root)
            elif self.var_mem_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required ",parent=self.root)
                cur.execute("select * from member")
            else:
                cur.execute("Select * from member where "+self.var_mem_searchby.get()+" LIKE '%"+self.var_mem_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!= 0:
                    self.MemberTable.delete(*self.MemberTable.get_children())
                    for row in rows:
                        self.MemberTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No Record Found",parent=self.root)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            


if __name__ == "__main__":
    root = Tk()
    obj = memberClass(root)
    root.mainloop()