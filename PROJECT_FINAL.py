# Project on Student Database Management System
import mysql.connector as driver
from prettytable import PrettyTable
import sys
def menu():
        print("\n1. INSERT RECORD")
        print("2. UPDATE RECORD")
        print("3. DELETE RECORD")
        print("4. SEARCH RECORD")
        print("5. DISPLAY RECORD")
        print("6. BACK TO TABLES")
        print()

def tables():
    while True:
        print("\n........CHOOSE TABLE.......")
        print("1. Subjects")
        print("2. Teachers")
        print("3. Student and Teachers ID")
        print("4. Students")
        print("5. Grades")
        print("6. QUIT")
        print()
        choice=int(input("Enter the choice (1-6) : "))
        if(choice==1):
                l="y"
                while l=="y":
                    menu()
                    option=int(input("Enter the option (1-6) : "))
                    if(option==1):
                        sub_insert_record()
                    elif(option==2):
                        sub_update_record()
                    elif(option==3):
                        sub_delete_record()
                    elif(option==4):
                        sub_search_record()
                    elif(option==5):
                        sub_display_record()
                    elif(option==6):
                        break
                    else:
                        print("incorrent option")
                    l=input("\nDo you want to continue?(y or n)")
                else:
                    sys.exit()
        elif(choice==2):
                l="y"
                while l=="y":
                    menu()
                    option=int(input("Enter the choice (1-5) : "))
                    if(option==1):
                        tea_insert_record()
                    elif(option==2):
                        tea_update_record()
                    elif(option==3):
                        tea_delete_record()
                    elif(option==4):
                        tea_search_record()
                    elif(option==5):
                        tea_display_record()
                    elif(option==6):
                        break
                    else:
                        print("incorrent option")
                    l=input("\nDo you want to continue?(y or n)")
                else:
                    sys.exit()
        elif(choice==3):
            l="y"
            while l=="y":
                menu()
                option=int(input("Enter the choice (1-5) : "))
                if(option==1):
                        stu_tea_insert_record()
                elif(option==2):
                        stu_tea_update_record()
                elif(option==3):
                        stu_tea_delete_record()
                elif(option==4):
                        stu_tea_search_record()
                elif(option==5):
                        stu_tea_display_record()
                elif(option==6):
                        break
                else:
                        print("incorrent option")
                l=input("\nDo you want to continue?(y or n)")
            else:
                    sys.exit()
        elif(choice==4):
            l="y"
            while l=="y":
                menu()
                option=int(input("Enter the choice (1-5) : "))
                if(option==1):
                        stu_insert_record()
                elif(option==2):
                        stu_update_record()
                elif(option==3):
                        stu_delete_record()
                elif(option==4):
                        stu_search_record()
                elif(option==5):
                        stu_display_record()
                elif(option==6):
                        break
                else:
                        print("incorrent option")
                l=input("\nDo you want to continue?(y or n)")
            else:
                    sys.exit()
        elif(choice==5):
            l="y"
            while l=="y":
                menu()
                option=int(input("Enter the choice (1-5) : "))
                if(option==1):
                        gra_insert_record()
                elif(option==2):
                        gra_update_record()
                elif(option==3):
                        gra_delete_record()
                elif(option==4):
                        gra_search_record()
                elif(option==5):
                        gra_display_record()
                elif(option==6):
                        break
                else:
                        print("incorrent option")
                l=input("\nDo you want to continue?(y or n)")
            else:
                    sys.exit()
        elif(choice==6):
            break
        else:
            print("Wrong Choice.Try again")
            

#functions for subject table
def sub_insert_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        try:
                cur=con.cursor()
                rollno=int(input("ENTER ID: "))
                NAME=input("ENTER Name OF subject: ")
                
                query1="INSERT INTO subjects(id,name) VALUES({},'{}')".format(rollno,NAME if NAME else null)
                cur.execute(query1)
                con.commit()
                print('Record Inserted')
                con.close()
        except Exception as e:
                print(f"Error: {e}")
    else:
        print("Error : Not Connected")

def sub_update_record():
        try:
            con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
            cur=con.cursor()
            d=int(input("Enter the id: "))
            name=input("ENTER NEW Name of subject : ")
            query1="update subjects set name='%s' where id=%s" %(name if name else null,d)
            cur.execute(query1)
            con.commit()
            print("Record Updated")
            con.close()
        except Exception as e:
                print(f"Error: {e}")

def sub_delete_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    d=int(input("Enter the id : "))
    query1="delete from subjects where id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def sub_search_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    d=int(input("Enter the ID: "))
    query1="select * from subjects where id=%s" %(d)
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    Table=PrettyTable(["ID","Name"])
    for i in rec:
        Table.add_row([i[0],i[1]])
    print(Table)
    con.close()

def sub_display_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from subjects')
        rec=cur.fetchall()
        count=cur.rowcount
        print("Total no. of records are : ",count)
        Table=PrettyTable(["ID","Name"])
        for i in rec:
            Table.add_row([i[0],i[1]])
        print(Table)
        con.close()
    else:
        print("Error : Database Connection is not success")

#functions for students_teachers
def stu_tea_insert_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        try:
                print("Successfully Connected")
                cur=con.cursor()
                Id=int(input("enter the id: "))
                teacher_id=int(input("enter teacher id: "))
                student_id=int(input("enter student id: "))
                query1="INSERT INTO students_teachers(id,teacher_id,student_id) VALUES({},{},{})".format(Id,teacher_id if teacher_id else null,student_id if student_id else null)
                cur.execute(query1)
                con.commit()
                print('Record Inserted')
                con.close()
        except Exception as e:
                print(f"Error: {e}")
    else:
        print("Error : Not Connected")

def stu_tea_update_record():
    try:
            con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
            cur=con.cursor()
            Id=int(input("Enter id you want to update: "))
            teacher_id=int(input("enter the new teacher_id:  "))
            student_id=int(input("enter the new student_id:"))
            query1="update students_teachers set teacher_id=%s, student_id=%s where id=%s" %(teacher_id if teacher_id else null,student_id if student_id else null,Id)
            cur.execute(query1)
            con.commit()
            print("Record Updated")
            con.close()
    except Exception as e:
                print(f"Error: {e}")

def stu_tea_delete_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    Id=int(input("Enter id you want to delete from table: "))
    query1="delete from students_teachers where id={0}".format(Id)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def stu_tea_search_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    Id=int(input("Enter id number you want to search: "))
    query1="select * from students_teachers where id=%s" %(Id)
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    table=PrettyTable(["ID","Teacher_ID","Student_ID"])
    for i in rec:
        table.add_row([i[0],i[1],i[2]])
    print(table)
    con.close()

def stu_tea_display_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from students_teachers')
        rec=cur.fetchall()
        count=cur.rowcount
        print("Total no. of records are : ",count)  
        table=PrettyTable(["ID","Teacher_ID","Student_ID"])
        for i in rec:
            table.add_row([i[0],i[1],i[2]])
        print(table)
        con.close()
    else:
        print("Error : Database Connection is not success")

#functions for teachers table
def tea_insert_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        try:
                cur=con.cursor()
                id_no=int(input("Enter teacher's id : "))
                q = "select * from teachers where id=%s" %(id_no)
                cur.execute(q)
                rec=cur.fetchall()
                count1=cur.rowcount
                if count1==0:
                    first_name=input("Enter the first name of teacher: ")
                    last_name=input("Enter the last name of teacher: ")
                    phone_number=int(input("Enter the phone number of teacher: "))
                    email_address=input("Enter the email address of teacher: ")
                    query1="INSERT INTO teachers(id,first_name,last_name,phone_number,email_address) VALUES({},'{}','{}',{},'{}')".format(id_no,first_name if first_name else null,last_name if last_name else null,phone_number,email_address if email_address else null)
                    cur.execute(query1)
                    con.commit()
                    print('Record Inserted')
                    con.close()
                else:
                    print("Record with entered ID exists")
        except Exception as e:
                print(f"Error: {e}")
    else:
        print("Error : Not Connected")

def tea_update_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        try:
                cur=con.cursor()
                d=int(input("Enter the id of the teacher's record you want to update: "))
                q2 = "select * from teachers where id=%s" %(d)
                cur.execute(q2)
                rec=cur.fetchall()
                count2=cur.rowcount
                if count2!=0:
                    id_no=int(input("Enter teacher's NEW id : "))
                    q3 = "select * from teachers where id=%s" %(id_no)
                    cur.execute(q3)
                    rec=cur.fetchall()
                    count3=cur.rowcount
                    if count3==0 or id_no==d:
                        first_name=input("Enter the NEW first name of teacher: ")
                        last_name=input("Enter the NEW last name of teacher: ")
                        phone_number=int(input("Enter the NEW phone number of teacher: "))
                        email_address=input("Enter the NEW email address of teacher: ")
                        query2="update teachers set id=%s, first_name='%s', last_name='%s' , phone_number=%s , email_address='%s' where id=%s" %(id_no,first_name if first_name else null,last_name if last_name else null,phone_number,email_address if email_address else null,d)
                        cur.execute(query2)
                        con.commit()
                        print("Record Updated")
                        con.close()
                    else:
                        print("Record with entered ID already exists")
                else:
                    print("Record does not exist")
        except Exception as e:
                print(f"Error: {e}")
    else:
        print("Error : Not Connected")


def tea_delete_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        cur=con.cursor()
        cur.execute('select * from teachers')
        rec=cur.fetchall()
        count=cur.rowcount
        if count>0:
            d=int(input("Enter the id of the teacher's record you want to delete: "))
            q4 = "select * from teachers where id=%s" %(d)
            cur.execute(q4)
            rec=cur.fetchall()
            count4=cur.rowcount
            if count4!=0:
                query3="delete from teachers where id={0}".format(d)
                cur.execute(query3)
                con.commit()
                print("Record Deleted")
                con.close()
            else:
                print("Record with entered ID does not exist")
        else:
            print("There is no record in the Teachers table")
    else:
        print("Error : Not Connected")

def tea_search_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        cur=con.cursor()
        d=int(input("Enter teacher ID: "))
        query4="select * from teachers where id=%s" %(d)
        cur.execute(query4)
        rec=cur.fetchall()
        count=cur.rowcount
        print("Total no. of records found according to given input: ",count)
        Table=PrettyTable(["ID","First Name","Last Name","Phone Number","Email Address"])
        for i in rec:
            table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(table)
        con.close()
    else:
        print("Error : Not Connected")

def tea_display_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        cur=con.cursor()
        cur.execute('select * from teachers')
        rec=cur.fetchall()
        count=cur.rowcount
        Table=PrettyTable(["ID","First Name","Last Name","Phone Number","Email Address"])
        for i in rec:
            Table.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(Table)
        con.close()
    else:
        print("Error : Not Connected")

#functions for students tables
def stu_insert_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        try:
                print("Successfully Connected")
                cur=con.cursor()
                Student_ID=int(input("Enter the Student ID: "))
                First_Name=input("Enter First Name of the student : ")
                Last_Name=input("Enter Last Name of the student : ")
                Phone_Number=int(input("Enter Phone Number of the student : "))
                Email_Address=input("Enter Email of the student : ")
                Grade_ID=int(input("ENTER Student Grade ID: "))
                query1="INSERT INTO students(id,first_name,last_name,phone_number,email_address,grade_id) VALUES({},'{}','{}',{},'{}',{})".format(Student_ID if Student_ID else null,First_Name if First_Name else null,Last_Name if Last_Name else null, Phone_Number, Email_Address if Email_Address else null, Grade_ID)
                cur.execute(query1)
                con.commit()
                print('Record Inserted')
                con.close()
        except Exception as e:
                print(f"Error: {e}")
    else:
        print("Error : Not Connected")

def stu_update_record():
        try:
            con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
            cur=con.cursor()
            d=int(input("Enter Student ID to update record : "))
            First_Name=input("Enter Updated First Name of the student : ")
            Last_Name=input("Enter Updated Last Name of the student : ")
            Phone_Number=int(input("Enter Updated Phone Number of the student : "))
            Email_Address=input("Enter new Email of the student : ")
            Grade_ID=int(input("ENTER new Student Grade ID : "))
            query1="update students set First_Name='%s', Last_Name='%s', Phone_Number=%s, Email_Address='%s',Grade_ID=%s where id=%s" %(First_Name if First_Name else null,Last_Name if Last_name else null, Phone_Number, Email_Address if Email_address else null,Grade_ID,d)
            cur.execute(query1)
            con.commit()
            print("Record Updated")
            con.close()
        except Exception as e:
                print(f"Error: {e}")

def stu_delete_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    d=int(input("Enter Student_ID to delete the record : "))
    query1="delete from students where id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def stu_search_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    d=int(input("Enter Student ID that has to be searched : "))
    query1="select * from students where id=%s" %(d)
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    table=PrettyTable(["ID","First_Name","Last_Name","Phone_Number","Email_address","Grade_Id"])
    for i in rec:
        table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
    print(table)
    con.close()

def stu_display_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from students')
        rec=cur.fetchall()
        count=cur.rowcount
        table=PrettyTable(["ID","First_Name","Last_Name","Phone_Number","Email_address","Grade_Id"])
        for i in rec:
            table.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(table)
        con.close()
    else:
        print("Error : Database Connection is not success")


#functions for grades table
def gra_insert_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        try:
                print("Successfully Connected")
                cur=con.cursor()
                Id=int(input("ENTER ID: "))
                NAME=input("ENTER Name OF letter: ")
                query1="INSERT INTO grades(id,letter) VALUES({},'{}')".format(Id,NAME if NAME else null)
                cur.execute(query1)
                con.commit()
                print('Record Inserted')
                con.close()
        except Exception as e:
                print(f"Error: {e}")
    else:
        print("Error : Not Connected")

def gra_update_record():
        try:
            con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
            cur=con.cursor()
            d=int(input("Enter the id: "))
            name=input("ENTER NEW Letter of grade : ")
            query1="update grades set letter='%s' where id=%s" %(name if name else null,d)
            cur.execute(query1)
            con.commit()
            print("Record Updated")
            con.close()
        except Exception as e:
                print(f"Error: {e}")

def gra_delete_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    d=int(input("Enter the id : "))
    query1="delete from grades where id={0}".format(d)
    cur.execute(query1)
    con.commit()
    print("Record Deleted")
    con.close()

def gra_search_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    cur=con.cursor()
    d=int(input("Enter the ID: "))
    query1="select * from grades where id=%s" %(d)
    cur.execute(query1)
    rec=cur.fetchall()
    count=cur.rowcount
    print("Total no. of records found : ",count)
    Table=PrettyTable(["ID","Letter"])
    for i in rec:
        Table.add_row([i[0],i[1]])
    print(Table)
    con.close()

def gra_display_record():
    con=driver.connect(host='localhost',user='root',passwd='12345',charset='utf8',database='stu_db',port="3307")
    if con.is_connected():
        print("Successfully Connected")
        cur=con.cursor()
        cur.execute('select * from grades')
        rec=cur.fetchall()
        count=cur.rowcount
        print("Total no. of records are : ",count)
        Table=PrettyTable(["ID","Letter"])
        for i in rec:
            Table.add_row([i[0],i[1]])
        print(Table)
        con.close()
    else:
        print("Error : Database Connection is not success")


#main
print("........STUDENT DATABASE MANAGEMENT SYSTEM.......")
con=driver.connect(host="localhost",user="root",passwd="12345",port="3307",charset='utf8',database='stu_db')
cur=con.cursor()
cur.execute("create table if not exists students_teachers(id int PRIMARY KEY, teacher_id int not null, student_id int not null)")
cur.execute("create table if not exists subjects(id int PRIMARY KEY, name varchar(15) not null)")
cur.execute("create table if not exists grades(id int PRIMARY KEY, letter varchar(20) not null)")
cur.execute("create table if not exists teachers(id integer primary key, first_name char(20) not null, last_name char(20) not null, phone_number BIGINT(12) not null,email_address varchar(20) not null unique)")
cur.execute("create table if not exists students(id int PRIMARY KEY, first_name varchar(15) not null,last_name varchar(15) not null, phone_number int not null,email_address char(20) not null unique, grade_id int not null)")
con.close()
tables()
