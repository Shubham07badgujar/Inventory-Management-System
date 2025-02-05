from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox, filedialog
import sqlite3

class productClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System | Team Third Axis")
        self.root.config(bg="white")
        self.root.focus_force()

        # Variables (as in your original code)
        self.var_cat = StringVar()
        self.var_invoice_no = StringVar()
        self.var_invoice_date = StringVar()
        self.var_price_item = StringVar()
        self.var_inovice_amount = StringVar()
        self.var_supp_name = StringVar()
        self.var_mo_no = StringVar()
        self.var_email_vendor = StringVar()
        self.var_received_std_name = StringVar()
        self.var_received_mo_no = StringVar()
        self.var_curr_posi = StringVar()
        self.var_curr_mo_no = StringVar()

        self.var_mem_searchby = StringVar()
        self.var_mem_searchtxt = StringVar()

        # Product frame
        product_Frame = Frame(self.root, bd=5, relief=RIDGE)
        product_Frame.place(x=10, y=10, width=650, height=800)

        # Title
        title = Label(product_Frame, text="Manage Product Details", font=("goudy old style", 20), bg="#0f4d7d", fg="white").pack(side=TOP, fill=X)

        # Labels and Entry fields (as per your original code)
        lbl_Invoice_number = Label(product_Frame, text="Invoice Number:", font=("goudy old style", 20)).place(x=30, y=60)
        lbl_product_name = Label(product_Frame, text="Product Name:", font=("goudy old style", 20)).place(x=30, y=110)
        lbl_Invoice_date = Label(product_Frame, text="Invoice Date:", font=("goudy old style", 20)).place(x=30, y=160)
        lbl_Price_of_the_item = Label(product_Frame, text="Price of the Item:", font=("goudy old style", 20)).place(x=30, y=210)
        lbl_Invoice_Amount = Label(product_Frame, text="Total Invoice Amount:", font=("goudy old style", 20)).place(x=30, y=260)
        lbl_supplier_name = Label(product_Frame, text="Supplier Name:", font=("goudy old style", 20)).place(x=30, y=310)
        lbl_mobile_number = Label(product_Frame, text="Mobile Number of Vendor:", font=("goudy old style", 20)).place(x=30, y=360)
        lbl_email_vendor = Label(product_Frame, text="Email of Vendor:", font=("goudy old style", 20)).place(x=30, y=410)
        lbl_received_by_student_name = Label(product_Frame, text="Received by Student Name:", font=("goudy old style", 20)).place(x=30, y=460)
        lbl_received_mo_no = Label(product_Frame, text="Received by Student Mob No.:", font=("goudy old style", 20)).place(x=30, y=510)
        lbl_curr_posi_name = Label(product_Frame, text="Currently Position:", font=("goudy old style", 20)).place(x=30, y=560)
        lbl_curr_posi_no = Label(product_Frame, text="Currently Number:", font=("goudy old style", 20)).place(x=30, y=610)

        # Entry fields
        txt_name = Entry(product_Frame, textvariable=self.var_invoice_no, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=60, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_cat, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=110, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_invoice_date, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=160, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_price_item, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=210, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_inovice_amount, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=260, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_supp_name, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=310, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_mo_no, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=360, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_email_vendor, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=410, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_received_std_name, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=460, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_received_mo_no, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=510, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_curr_posi, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=560, width=200)
        txt_name = Entry(product_Frame, textvariable=self.var_curr_mo_no, font=("goudy old style", 15), bg='lightyellow').place(x=370, y=610, width=200)

        # Buttons
        btn_add = Button(product_Frame, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=10, y=700, width=100, height=40)
        btn_update = Button(product_Frame, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=120, y=700, width=100, height=40)
        btn_delete = Button(product_Frame, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=230, y=700, width=100, height=40)
        btn_clear = Button(product_Frame, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=340, y=700, width=100, height=40)
        
        # Upload button
        btn_upload = Button(product_Frame, text="Upload", command=self.openFile, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=450, y=700, width=100, height=40)

        # Other parts of the GUI
        # (Search Frame and Product Details are as per your original code)

    # Function to open the file dialog and read the file
    def openFile(self):
        filepath = filedialog.askopenfilename(initialdir="C://Users//HP//Desktop//Inventory-Management-System",
                                              title="Open file okay?",
                                              filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if filepath:
            with open(filepath, 'r') as file:
                print(file.read())

    # Other methods (add, update, delete, clear, etc.)
    # ...

if __name__ == "__main__":
    root = Tk()
    obj = productClass(root)
    root.mainloop()
