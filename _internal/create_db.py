import sqlite3
def create_db():
    con = sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS member(memid INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, pass text, utype text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()
                                                        # "Product Name","Invoice number","Invoice date","Price","Total Invoice Amount","Supplier Name","Vendor MO NO","Email of vendor","R Student Name","R Std Mo No","Current position","Current Mo No"
    # cur.execute("CREATE TABLE IF NOT EXISTS product(Invoice_number INTEGER PRIMARY KEY AUTOINCREMENT,Product Name text,Invoice date text,Price text,Total Invoice Amount text,Supplier Name text,Vendor MO NO text,Email of vendor text,R Student Name text,R Std Mo No text,Current position text,Current Mo No text)")
    # con.commit()

    cur.execute("""
            CREATE TABLE IF NOT EXISTS product(
                Invoice_number TEXT PRIMARY KEY , 
                [Product Name] TEXT, 
                [Invoice date] TEXT, 
                Price TEXT, 
                qty INTEGER,
                [Total Invoice Amount] TEXT, 
                [Supplier Name] TEXT, 
                [Vendor MO NO] TEXT, 
                [Email of vendor] TEXT, 
                [R Student Name] TEXT, 
                [R Std Mo No] TEXT, 
                [Current position] TEXT, 
                [Current Mo No] TEXT,
                pdf_file BLOB
                PDF_path TEXT
                
            )
        """)
    con.commit()

    
    
    

create_db()