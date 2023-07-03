def about():
    f=open("About.txt","r")
    ch=f.readlines()
    for i in ch:
        print(i)
    f.close()
about()
    
#ESTABLISHING CONNECTIVITY
import mysql.connector as c
con=c.connect(host="localhost",user="root",passwd="root",database="library")
cur=con.cursor()

#TO ADD DETAILS OF A STUDENT
def addstd():
    sid=int(input("Enter student id:"))
    sname=input("Enter name of student:").upper()
    cls=input("Enter class and division:").upper()
    cur.execute("insert into student values({},'{}','{}')".format(sid,sname,cls))
    con.commit()
    print("The details have been successfully added\n\n")

#TO DISPLAY DETAILS OF STUDENTS
def dispstd():
    cur.execute("select * from student")
    t=cur.fetchall()
    for i in t:
        print(i)

#TO DELETE DETAILS OF A STUDENT
def delstd():
    sid=int(input("Enter student id of student to be deleted:"))
    cur.execute("select * from student where sid={}".format(sid))
    t=cur.fetchall()
    if len(t)!=0:
        cur.execute("delete from student where sid={}".format(sid))
        con.commit()
        print("The details have been successfully deleted\n")
    else:
        print("no such student found\n")

#TO SEARCH FOR A STUDENT
def searchstd():
    sname=input("Enter name of student to be searched:")
    cur.execute("select* from student where sname='{}'".format(sname))
    t=cur.fetchall()
    if len(t)==0:
        print("Student does not exist\n")
    else:
        for i in t:
            print(i)



#TO ADD DETAILS OF A BOOK
def addbook():
    bid=int(input("Enter book id:"))
    bname=input("Enter name of book:").upper()
    author=input("Enter name of author:").upper()
    type=input("Enter type of book:").upper()
    price=int(input("Enter price of book:"))
    cur.execute("insert into book(bid,bname,author,type,price) values({},'{}','{}','{}',{})".format(bid,bname,author,type,price))
    con.commit()
    print("The details have been successfully added\n")

#TO DISPLAY DETAILS OF BOOKS
def dispbook():
    cur.execute("select * from book")
    t=cur.fetchall()
    for i in t:
        print(i)
    print()

#TO DELETE DETAILS OF A BOOK
def delbook():
     bid=int(input("Enter book id of book to be deleted:"))
     cur.execute("delete from book where bid={}".format(bid))
     con.commit()
     cur.execute("update book set status='IN' where bid={}".format(bid))
     print("The details have been successfully deleted\n")

#TO SEARCH FOR A BOOK
def searchbook():
    while True:
        print("SEARCH MENU")
        print("----------------")
        print("1.Search  by id")
        print("2.Search  by book name")
        print("3.Search  by author")
        print("4.Search  by type")
        print("5.Go back\n\n")
        chsrm=int(input("Enter choice:"))#chsrm-choice in search menu
        
        if chsrm==1:#TO SEARCH BY BOOK ID
            bid=int(input("Enter book id to be searched:"))
            cur.execute("select * from book where bid={}".format(bid))
            t=cur.fetchall()
            for i in t:
                print(i)
        elif chsrm==2:#TO SEARCH  BY BOOK NAME
            cur.execute("select bname from book")
            b=cur.fetchall()
            for i in b:
                print(i)
            bname=input("Enter name of book to be searched:").upper()
            cur.execute("select * from book where bname='{}'".format(bname))
            t=cur.fetchall()
            
            for i in t:
                print(i)
            print()
        
        elif chsrm==3:#TO SEARCH  BY AUTHOR
            cur.execute("select distinct author from book")
            t=cur.fetchall()
            for i in t:
                print(i)
            author=input("Enter name of author to be searched:").upper()
            cur.execute("select * from book where author='{}'".format(author))
            t=cur.fetchall()
            for i in t:
                print(i)
            print()
            
        elif chsrm==4:#TO SEARCH  BY TYPE OF BOOK
            cur.execute("select distinct type from book")
            t=cur.fetchall()
            print("type of books available are:")
            for i in t:
                for j in i:
                    print(j)
                print()
            
            type=input("Enter type of book to be searched:").upper()
            cur.execute("select * from book where type='{}'".format(type))
            t=cur.fetchall()
            if len(t)!=0:
                print("books available:")
                for i in t:
                    print(i)
            else:
                print("no books available")
            print()
            
        elif chsrm==5:
            break
        else:
            print("Invalid choice\n\n")

#TO ISSUE A BOOK
def issuebook():
    sid=int(input("Enter your student id:"))
    
    cur.execute("select * from student where sid={}".format(sid))
    s=cur.fetchall()
    if len(s) !=0:
        bid=int(input("Enter book id:"))
        cur.execute("select status from book where bid={}".format(bid))
        t=cur.fetchall()
        print(t[0][0])
        if t[0][0] in 'inIN':
            cur.execute("update book set status='OUT' where bid={}".format(bid))#status=out means book has already been issued and is not available in the library
            con.commit()
            print("book issued to",s[0][1],"\n")
        else:
            print("book not in shelf\n")
    else:
        print("student not from this school\n")

#TO RETURN A BOOK            
def returnbook():
    bid=int(input("Enter book id:"))
    cur.execute("update book set status='IN' where bid={}".format(bid))#status=in means book is available in the library  can change default in mysql
    con.commit()
    print("book is returned\n")


#MAIN PROGRAM  

while True:
    print("MAIN MENU")
    print("-------------")
    print("1.STUDENT")
    print("2.BOOK")
    print("3.EXIT\n\n")
    chmm=int(input("Enter choice:"))#chmm-choice in main menu
    
    if chmm==1:
        while True:
            print("STUDENT MENU")
            print("------------------")
            print("1.Add a student")
            print("2.Display student's details")
            print("3.Delete a student")
            print("4.Search a student")
            print("5.Go back\n\n")
            chstm=int(input("Enter choice:"))#chstm-choice in student menu
            print()
            if chstm==1:
                addstd()
            elif chstm==2:
                dispstd()
            elif chstm==3:
                delstd()
            elif chstm==4:
                searchstd()
            elif chstm==5:
                break
    elif chmm==2:
        while True:
            print("BOOK MENU")
            print("-------------")
            print("1.Add a book")
            print("2.Display a book's detail")
            print("3.Delete a book")
            print("4.Search a book")
            print("5.Issue a book")
            print("6.Return a book")
            print("7.Go back\n\n")
            chbm=int(input("Enter choice:"))#chbm-choice in book menu
            
            if chbm==1:
                addbook()
            elif chbm==2:
                dispbook()
            elif chbm==3:
                delbook()
            elif chbm==4:
                searchbook()
            elif chbm==5:
                issuebook()
            elif chbm==6:
                returnbook()
            elif chbm==7:
                break
            else :
                print("Invalid choice\n\n")

    elif chmm==3:
        print("Exiting.....THANK YOU:")
        break
    else:
        print("Invalid choice\n\n")
