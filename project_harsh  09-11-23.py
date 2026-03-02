import mysql.connector as cn
from datetime import date
db=cn.connect(host="localhost",user="root",password="",database="blood_bank")
cr=db.cursor()

def createTable():
         donar_table="CREATE TABLE IF NOT EXISTS donar_details(donar_id int AUTO_INCREMENT PRIMARY KEY,donar_name text,blood_group text,age int,contact_number text,location text,reg_date date)"    
         cr.execute(donar_table)
         db.commit()
         
         donar_table="CREATE TABLE IF NOT EXISTS receiver_details(receiver_id int AUTO_INCREMENT PRIMARY KEY,receiver_name text,blood_group text,age int,contact_number text,location text,reg_date date)"    
         cr.execute(donar_table)
         db.commit()
                 
def donar_reg():
    name=input("Enter Donar Name=")
    group=input("Enter Blood Group=")
    age=int(input("Enter Age="))
    contact=input("Enter Contact number=")
    location=input("Enter Location=")
    dt=date.today()
    cmd="INSERT INTO donar_details(donar_name, blood_group, age, contact_number, location,reg_date) VALUES(%s,%s,%s,%s,%s,%s)"
    data=(name,group,age,contact,location,dt)
    cr.execute(cmd,data)
    db.commit()
    print("Donar's Details Successfully Saved !!!\n")
         
def donar_details():
    cmd="SELECT * FROM donar_details"
    cr.execute(cmd)
    data=cr.fetchall()
    print("==============Donar's Details=================")
    for donar in data:
        print("Donar's Name=",donar[1])
        print("Blood Group=",donar[2])
        print("Age=",donar[3])
        print("Contact Number=",donar[4])
        print("Location=",donar[5])
        print("----------------------------------\n")
        
def bydate_donar_details():
    dt=input("Enter Date=")
    cmd="SELECT * FROM donar_details WHERE reg_date=%s"
    cr.execute(cmd,(dt,))
    data=cr.fetchall()
    print("==============Donar's Details=================")
    for donar in data:
        print("Donar's Name=",donar[1])
        print("Blood Group=",donar[2])
        print("Age=",donar[3])
        print("Contact Number=",donar[4])
        print("Location=",donar[5])
        print("----------------------------------\n")
        
def donar_list():
    cmd="SELECT * FROM donar_details"
    cr.execute(cmd)
    data=cr.fetchall()
    print("==============Donar's List=================")
    print("ID\tBlood Group \tDonar's Name")
    for donar in data:
        print(donar[0],"\t",donar[2],"\t\t",donar[1])
    print("----------------------------------\n")
        
def donar_search():
    group=input("Enter Blood Group=")
    cmd="SELECT * FROM donar_details WHERE blood_group=%s"
    data=(group,)
    cr.execute(cmd,data)
    data=cr.fetchall()
    print("==============Donar's Details By Blood Group=================")
    for donar in data:
        print("Donar's Name=",donar[1])
        print("Blood Group=",donar[2])
        print("Age=",donar[3])
        print("Contact Number=",donar[4])
        print("Location=",donar[5])
        print("----------------------------------\n")
            
def delete_donar():
    name=input("Enter Donar Name=")
    group=input("Enter Blood Group=")
    cmd="DELETE FROM donar_details WHERE donar_name=%s AND blood_group=%s"
    data=(name,group)
    cr.execute(cmd,data)
    db.commit()
    print("Donar's Record Successfully Deleted !!!\n")
    

def donar_update():
    ID=int(input("Enter Donar's ID="))
    name=input("Enter Donar's Name=")
    group=input("Enter Blood Group=")
    cmd="UPDATE donar_details SET donar_name=%s, blood_group=%s WHERE donar_id=%s "
    data=(name,group,ID)
    cr.execute(cmd,data)
    db.commit()
    print("Donar's Details Successfully Updated !!!\n")

def  blood_stock():
    cmd="SELECT blood_group,COUNT(donar_id) FROM donar_details GROUP BY blood_group"
    cr.execute(cmd)
    data=cr.fetchall()
    print("==============Donar's List=================")
    print("Blood Group \tStock")
    for donar in data:
        print(donar[0],"\t\t",donar[1],"\t")
    print("----------------------------------\n")

#------------------------------------------------------------------Receiver-------------------------------------------------------




def receiver_reg():
    name=input("Enter Receiver Name=")
    group=input("Enter Blood Group=")
    age=int(input("Enter Age="))
    contact=input("Enter Contact number=")
    location=input("Enter Location=")
    dt=date.today()
    cmd="INSERT INTO receiver_details(receiver_name, blood_group, age, contact_number, location,reg_date) VALUES(%s,%s,%s,%s,%s,%s)"
    data=(name,group,age,contact,location,dt)
    cr.execute(cmd,data)
    db.commit()
    print("Receiver's Details Successfully Saved !!!\n")
     
def receiver_details():
    cmd="SELECT * FROM receiver_details"
    cr.execute(cmd)
    data=cr.fetchall()
    print("==============Receiver's Details=================")
    for receiver in data:
        print("Receiver's Name=",receiver[1])
        print("Blood Group=",receiver[2])
        print("Age=",receiver[3])
        print("Contact Number=",receiver[4])
        print("Location=",receiver[5])
        print("----------------------------------\n")
    
def bydate_receiver_details():
    dt=input("Enter Date=")
    cmd="SELECT * FROM receiver_details WHERE reg_date=%s"
    cr.execute(cmd,(dt,))
    data=cr.fetchall()
    print("==============Receiver's Details=================")
    for receiver in data:
        print("Receiver's Name=",receiver[1])
        print("Blood Group=",receiver[2])
        print("Age=",receiver[3])
        print("Contact Number=",receiver[4])
        print("Location=",receiver[5])
        print("----------------------------------\n")
        
def receiver_list():
    cmd="SELECT * FROM receiver_details"
    cr.execute(cmd)
    data=cr.fetchall()
    print("==============Receiver's Details=================")
    print("ID\tBlood Group \Receiver's Name")
    for receiver in data:
      print(receiver[0],"\t",receiver[2],"\t\t",receiver[1])
    print("----------------------------------\n")
    
        
def receiver_search():
    group=input("Enter Blood Group=")
    cmd="SELECT * FROM receiver_details WHERE blood_group=%s"
    data=(group,)
    cr.execute(cmd,data)
    data=cr.fetchall()
    print("==============Receiver's Details By Blood Group=================")
    for receiver in data:
        print("Receiver's Name=",receiver[1])
        print("Blood Group=",receiver[2])
        print("Age=",receiver[3])
        print("Contact Number=",receiver[4])
        print("Location=",receiver[5])
        print("----------------------------------\n")
        
            
def delete_receiver():
    name=input("Enter Receiver Name=")
    group=input("Enter Blood Group=")
    cmd="DELETE FROM receiver_details WHERE receiver_name=%s AND blood_group=%s"
    data=(name,group)
    cr.execute(cmd,data)
    db.commit()
    print("Receiver's Record Successfully Deleted !!!\n")
       
def receiver_update():
    ID=int(input("Enter Receiver's ID="))
    name=input("Enter New Receiver's Name=")
    group=input("Enter New Blood Group=")
    cmd="UPDATE receiver_details SET receiver_name=%s, blood_group=%s WHERE receiver_id =%s "
    data=(name,group,ID)
    cr.execute(cmd,data)
    db.commit()
    print("Receiver's Details Successfully Updated !!!\n")
    
def donar_reciever_record():
    user_input=input("Enter User Name Or User ID=")
    cmd="SELECT *,'Donar' FROM donar_details WHERE donar_name=%s or donar_id=%s UNION ALL SELECT *,'Reciever' FROM receiver_details WHERE receiver_name=%s OR receiver_id=%s;"
    data=(user_input,user_input,user_input,user_input)
    cr.execute(cmd,data)
    data=cr.fetchall()
    print("=============Details=================")
    for user in data:
        print("Receiver's Name=",user[1])
        print("Blood Group=",user[2])
        print("Age=",user[3])
        print("Contact Number=",user[4])
        print("Location=",user[5])
        print("Type=",user[7])
        print("----------------------------------\n")
    
    
#----------------------------------------------------------------- Project Menu---------------------------------------         
createTable()

#--------------------------------------------
print("\n\n========================Welcome to Blood Bank========================\n\n")

while True:
    print("1. Donation:")
    print("2. Receiver:")
    print("3. User:")
    n=int(input("Enter Choice="))
    if n==1: 
         while True:
            print("\ta. Add New Donar")
            print("\tb. Exist Donar Details")
            print("\tc. Search Donar (by blood group)")
            print("\td. Delete Record (by name & blood group)")
            print("\te. Back")
            ch=input("\t Enter Choice:")
            if ch=='a':
                donar_reg()
            elif ch=='b':
                donar_details()
            elif ch=='c':
                donar_search()
            elif ch=='d':
                delete_donar()
            elif ch=='e':
                break;
            else:
                print("Invalid Choice")
    elif n==2: 
         while True:
            print("\ta. Add New Receiver")
            print("\tb. Exist Receiver Details")
            print("\tc. Search Receiver (by blood group)")
            print("\td. Delete Record (by name & blood group)")
            print("\te. Back")
            ch=input("\t Enter Choice:")
            if ch=='a':
                receiver_reg()
            elif ch=='b':
                receiver_details()
            elif ch=='c':
                receiver_search()
            elif ch=='d':
                delete_receiver()
            elif ch=='e':
                break;
            else:
                print("Invalid Choice")
    elif n==3: 
         while True:
            print("\ta. List (Donar & Receiver)")
            print("\tb. Edit Name or Blood Group")
            print("\tc. Delete Record (Donar or Receiver)")
            print("\td. Search Donar or Receiver (by blood group)")
            print("\te. Stock")
            print("\tf. Record By Date")
            print("\tg. Record By User Name or User ID")
            print("\th. Back")
            ch=input("\t Enter Choice:")
            if ch=='a':
                 while True:
                     print("1. Donar's List")
                     print("2. Receiver's List")
                     print("3. Back")
                     n=int(input("Enter Choice="))
                     if n==1:
                         donar_list()
                     elif n==2:
                         receiver_list()
                     elif n==3:
                         break;
                     else:
                         print("Invalid Choice")            
            elif ch=='b':
                while True:
                     print("1. Donar's Details Edit")
                     print("2. Receiver's Details Edit")
                     print("3. Back")
                     n=int(input("Enter Choice="))
                     if n==1:
                         donar_update()
                     elif n==2:
                         receiver_update()
                     elif n==3:
                         break;
                     else:
                         print("Invalid Choice")
            elif ch=='c':
                while True:
                     print("1. Delete Donar's Record")
                     print("2. Delete Receiver's Record")
                     print("3. Back")
                     n=int(input("Enter Choice="))
                     if n==1:
                         delete_donar()
                     elif n==2:
                         delete_receiver()
                     elif n==3:
                         break;
                     else:
                         print("Invalid Choice") 
            elif ch=='d':
                while True:
                     print("1. Search Donar's")
                     print("2. Search Receiver's")
                     print("3. Back")
                     n=int(input("Enter Choice="))
                     if n==1:
                        donar_search()
                     elif n==2:
                        receiver_search()
                     elif n==3:
                         break;
                     else:
                         print("Invalid Choice") 
            elif ch=='e':
                blood_stock()
            elif ch=='f':
                while True:
                     print("1. Today's Registred Donar")
                     print("2. Today's Registred Receiver")
                     print("3. Back")
                     n=int(input("Enter Choice="))
                     if n==1:
                        bydate_donar_details()
                     elif n==2:
                        bydate_receiver_details()
                     elif n==3:
                         break;
                     else:
                         print("Invalid Choice") 
            elif ch=='g':
                donar_reciever_record()
            elif ch=='h':
                break
            else:
                print("Invalid Choice")