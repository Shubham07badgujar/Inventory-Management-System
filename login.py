from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os
import email_pass
import smtplib  #pip install smtplib
import time

class LoginSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Login System | Team Third Axis")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        self.otp=''

        #==== images ==============
        self.phone_img=ImageTk.PhotoImage(file="Images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_img,bd=0).place(x=200,y=50)

        #===== Login Frame ===============
        self.member_id=StringVar()
        self.password=StringVar()

        loginFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        loginFrame.place(x=650,y=90,width=350,height=460)


        title=Label(loginFrame,text="Login System",font=("Elephant", 30, "bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(loginFrame,text="Member ID",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
        
        txt_member_id=Entry(loginFrame,textvariable=self.member_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)

        lbl_pass=Label(loginFrame,text="Paassword",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=200)
        txt_pass=Entry(loginFrame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(loginFrame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0F0",activebackground="#00B0F0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(loginFrame,bg="lightgrey").place(x=50,y=370,width=250,height=2)
        or_=Label(loginFrame,text="OR",bg="white",fg="lightgrey",font=("times new roman",15, "bold")).place(x=155,y=355)

        btn_forget=Button(loginFrame,text="Forget Password ?",command=self.forgetWindow,font=("times new roman",13),bg="white",fg="#00759E",bd=0,activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #=====Frame2======
        registerFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        registerFrame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(registerFrame,text="Team Third Axis | Beyond The Horizon",font=("times new roman",13),bg="white").place(x=40,y=18)
        
        #====Animation Images====== 
        self.im1=ImageTk.PhotoImage(file="Images/im1.png")
        self.im2=ImageTk.PhotoImage(file="Images/im2.png")
        self.im3=ImageTk.PhotoImage(file="Images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()

#=============== All Fucntions===================

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


    import sqlite3


    def login(self):
        try:
            member_id = self.member_id.get()
            password = self.password.get()

            if not member_id or not password:
                messagebox.showerror("Error", "All Fields are required", parent=self.root)
                return

            with sqlite3.connect('ims.db') as con:
                cur = con.cursor()

                # Check if there are any members in the table
                cur.execute("SELECT COUNT(*) FROM member")
                count = cur.fetchone()[0]

                if count == 0:
                    # No members exist, create the first admin member
                    cur.execute("INSERT INTO member (memid, pass, utype) VALUES (?, ?, ?)", (member_id, password, 'Admin'))
                    con.commit()
                    messagebox.showinfo("Info", "No members found. Created the first member as Admin.", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                else:
                    # Proceed with login as usual
                    cur.execute("SELECT utype FROM member WHERE memid=? AND pass=?", (member_id, password))
                    user = cur.fetchone()

                    if user is None:
                        messagebox.showerror("Error", "Invalid Member ID or Password", parent=self.root)
                    else:
                        self.root.destroy()
                        if user[0] == "Admin":
                            os.system("python dashboard.py")
                        else:
                            os.system("python product.py")

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    def forgetWindow(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.member_id.get()=="":
                messagebox.showerror("Error","Member ID must required",parent=self.root)
            else:
                cur.execute("select email from member where memid=? " ,(self.member_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror("Error","Invalid Member ID, try again",parent=self.root)
                else:
                    #==========forget window================
                    self.var_otp=StringVar()
                    self.var_new_password=StringVar()
                    self.var_conf_password=StringVar()
                    # call send_email_function()
                    chk=self.send_email(email[0])
                    if chk=='f':
                        messagebox.showerror("Error","Connection Error, Try again later",parent=self.root)
                    else:
                        self.forgetWind=Toplevel(self.root)
                        self.forgetWind.title("RESET PASSWORD")
                        self.forgetWind.geometry("400x350+500+100")
                        self.forgetWind.focus_force()

                        title=Label(self.forgetWind,text="Reset Password",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white").pack(side=TOP,fill=X)
                        lbl_reset=Label(self.forgetWind,text="Enter OTP sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                        txt_reset=Entry(self.forgetWind,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow",).place(x=20,y=100,width=250,height=30)
                        self.btn_reset=Button(self.forgetWind,text="Submit",command=self.validate_otp,font=("times new roman",15),bg="lightblue",)
                        self.btn_reset.place(x=280,y=100,width=100,height=30)

                        new_pass=Label(self.forgetWind,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                        txt_new_pass=Entry(self.forgetWind,textvariable=self.var_new_password,font=("times new roman",15),bg="lightyellow",).place(x=20,y=190,width=250,height=30)

                        conf_pass=Label(self.forgetWind,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                        txt_conf_pass=Entry(self.forgetWind,textvariable=self.var_conf_password,font=("times new roman",15),bg="lightyellow",).place(x=20,y=255,width=250,height=30)

                        self.btn_update=Button(self.forgetWind,text="Update",command=self.update_password,state=DISABLED,font=("times new roman",15),bg="lightblue",)
                        self.btn_update.place(x=150,y=300,width=100,height=30)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def update_password(self):
        if self.var_new_password.get()=="" or self.var_conf_password.get()=="":
            messagebox.showerror("Error","Password is required",parent=self.forgetWind)
        elif self.var_new_password.get()!= self.var_conf_password.get():
            messagebox.showerror("Error","New Password & Confirm Password should be same",parent=self.forgetWind)
        else:
            con=sqlite3.connect(database=r'ims.db')
            cur=con.cursor()
            try:
                cur.execute("Update member SET pass=? where memid=?",(self.var_new_password.get(),self.member_id.get(),))
                con.commit()
                messagebox.showinfo("Success","Password Updated Successfully !",parent=self.forgetWind)
                self.forgetWind.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def validate_otp(self):
        if int(self.otp)==int(self.var_otp.get()):
            self.btn_update.config(state=NORMAL)
            self.btn_reset.config(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid OTP ! Try Again",parent=self.forgetWind)

        
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime("%H%S%M"))+int(time.strftime("%S"))
        
        subj="Team Third Axis \nInventory Management System \nReset Password OTP"
        msg=f"Dear Sir/Madam, \n\nYour Reset OTP is {str(self.otp)}.\n\nWith Regards, \nTeam Third Axis"
        msg="Subject:{}\n\n{}".format(subj,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'

root=Tk()
obj=LoginSystem(root)
root.mainloop()