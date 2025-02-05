from tkinter import*
from PIL import Image, ImageTk
from member import memberClass
from product import productClass
from supplier import supplierClass
import sqlite3
from tkinter import messagebox
import time
import os

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Team Third Axis | GCOEJ")
        self.root.config(bg = "white")

        #== title ==
        # self.icon_title = PhotoImage(file="")
        self.icon_title = Image.open("Images/thirdaxislogo1.png")
        self.icon_title = self.icon_title.resize((70,70),Image.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman", 40, "bold"),bg="red",fg="white",anchor="w", padx=20).place(x = 0, y = 0, relwidth=1, height= 70)

        


        #== button_logout ==
        btn_logout = Button(self.root, text="Logout",command=self.logout, font=("times new roman", 15, "bold"), bg = "white",cursor="hand2").place(x=1350, y=10, height=50, width=150)

        # == Clock == 
        self.lbl_clock = Label(self.root, text="Welcome to Inventory Management System \t\t Date : DD-MM-YYYY \t\t Time : HH:MM:SS ", font=("times new roman", 15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x = 0, y = 70, relwidth=1, height= 30)

        # == Left Menu ==
        self.MenuLogo = Image.open("Images/menu_im.png")
        self.MenuLogo = self.MenuLogo.resize((200,200),Image.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root,bd=2,relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=460)

        lbl_menuLogo = Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)


        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg = "#009688").pack(side=TOP,fill=X)
        btn_employee = Button(LeftMenu, text="Members",command=self.member, font=("times new roman", 20, "bold"), bg = "white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier",command=self.supplier, font=("times new roman", 20, "bold"), bg = "white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu, text="Product",command=self.product, font=("times new roman", 20, "bold"), bg = "white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        # btn_sales = Button(LeftMenu, text="Sales",command=self.sales, font=("times new roman", 20, "bold"), bg = "white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        btn_employee = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg = "white", bd=3, cursor="hand2").pack(side=TOP,fill=X)
        # btn_employee = Button(LeftMenu, text="Exit", font=("times new roman", 20, "bold"), bg = "white", bd=3, cursor="hand2").pack(side=TOP,fill=X)


        # ===== Content =====

        self.lbl_member = Label(self.root, text="Total Members \n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9", fg="white",font=("goudy old style",20,"bold"))
        self.lbl_member.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier \n[ 0 ]",bd=5,relief=RIDGE,bg="lightblue", fg="white",font=("goudy old style",20,"bold"))
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_product = Label(self.root, text="Total Products \n[ 0 ]",bd=5,relief=RIDGE,bg="#ff00ff", fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=1000,y=120,height=150,width=300)

        # self.lbl_category = Label(self.root, text="Total Sales \n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9", fg="white",font=("goudy old style",20,"bold"))
        # self.lbl_category.place(x=300,y=300,height=150,width=300)

        # self.lbl_sales = Label(self.root, text="Total Members \n[ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9", fg="white",font=("goudy old style",20,"bold"))
        # self.lbl_sales.place(x=650,y=300,height=150,width=300)
        

        # ==== footer ====
        lbl_footer = Label(self.root, text="Inventory Management System | Team Third Axis | GCOEJ", font=("times new roman", 12),bg="#4d636d",fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()

#=====================================================================================================================================================================================
    def member(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = memberClass(self.new_win)

#=========================================================================================================================================================================================

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = productClass(self.new_win)

    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Products\n {str(len(product))}")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f"Total Suppliers\n {str(len(supplier))}")

            cur.execute("select * from member")
            member=cur.fetchall()
            self.lbl_member.config(text=f"Total Members\n {str(len(member))}")

           
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System \t\t Date : {str(date_)} \t\t Time : {str(time_)} ")
            self.lbl_clock.after(200,self.update_content)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
            

    def logout(self):
        self.root.destroy()
        os.system("python login.py")

    


if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()