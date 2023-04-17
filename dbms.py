# START

# Importing Modules and Packages
import mysql.connector
from mysql.connector import Error
import time

# Initializing Variables (Global etc.)
opt = ''
list1 = []
fo = 0

# Opening a .TXT file
fo = open('ChapterView.txt', 'r+')

# Open database connection
conDict = {"host":"localhost",
          "database": "library",
          "user":"root",
          "password":""}

try:
    db = mysql.connector.connect (**conDict)
    if db.is_connected():
        
# Executing SQL queries by Defining Functions

# Defining Search Function
        def search():
            'This Function is to Search Books'
            print("\nYou are about to search for Books")
            print ()
            time.sleep(1)
            print ('''Choose an option to start the query
1. Book Number
2. Book Title
3. Author
4. Publisher
5. Subject category
6. Select All Books''')
            print()
            # Query Option INPUT
            opt = input("Choose an option (1/2/3/4/5/6) : ")
            if opt == '1' or opt == '2' or opt == '3' or opt == '4' or opt == '5' or opt == '6' :
                if opt == '1':
                    bno =  input("Enter the Book Number : ")
                    cursor = db.cursor()
                    sql = ('SELECT * FROM book WHERE BookNo = %s')
                    data = bno
                    cursor.execute(sql,[data])
                    result = cursor.fetchall()
                    print ('\n',cursor.rowcount," Book Search found")
                    # Output
                    for i in result:
                        print ("—————————————————————————")
                        print ('<<<Book Number>>> : ',i[0])
                        print ('Book Title : ', i[1],)
                        print ('Subject Code : ', i[2])
                        print ('Author : ', i[3])
                        print ('Publisher : ', i[4])
                        print ('Price : ', i[5])
                        print ('Location : ', i[6])
                        print ("——————————————————————————")
   
                elif opt == '2':
                    bName = input("Enter the Book Title : ")
                    cursor = db.cursor()
                    sql = (f"SELECT * FROM book WHERE Title LIKE '%{bName}%'")
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print ('\n',cursor.rowcount," Book Search found")
                    for i in result:
                        print ("_____________________________________________________________________________________________________________________________________________________")
                        print(f"Book Number : {i[0]} | <<<Book Title>>> : {i[1]} | Subject Code : {i[2]} | Author : {i[3]} | Publisher : {i[4]} | Price : {i[5]} | Location : {i[6]} " )
                    
                elif opt == '3':
                    bAut = input("Enter Author Name : ")
                    cursor = db.cursor()
                    sql = (f"SELECT * FROM book WHERE Author LIKE '%{bAut}%'")
                    data = (bAut)
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print ('\n',cursor.rowcount," Book Search found")
                    # Output
                    for i in result:
                        print ("—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
                        print(f"Book Number : {i[0]} | Book Title : {i[1]} | Subject Code : {i[2]} | <<<Author>>> : {i[3]} | Publisher : {i[4]} | Price : {i[5]} | Location : {i[6]} " )
                               
                elif opt == '4':
                    bPub = input("Enter Publisher Name : ")
                    cursor = db.cursor()
                    sql = (f"SELECT * FROM book WHERE Publisher LIKE '%{bPub}%'")
                    
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print ('\n',cursor.rowcount," Book Search found")
                    # Output
                    for i in result:
                        print ("__________________________________________________________________________________________________________________________________________________")
                        print(f"Book Number : {i[0]} | Book Title : {i[1]} | Subject Code : {i[2]} | Author : {i[3]} | <<<Publisher>>> : {i[4]} | Price : {i[5]} | Location : {i[6]} " )
                    
                elif opt == '5':
                    print()
                    print ('''1) ART - ARTS
2) LIFESTYLE - LIFE
3) ENGLISH - ENG
4) HISTORY - HIS
5) Fantasy - FAN
6) OTHER''')
                    sName = input("Enter the  subject Code (ARTS/ENG/HIS etc.) : ")
                    sName = sName.upper()
                    cursor = db.cursor()
                    sql = (f"SELECT * FROM book WHERE SubjectCode LIKE '%{sName}%'")
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    print ('\n',cursor.rowcount," Book Search found")
                    # Output
                    for i in result:
                        print ("_________________________________________________________________________________________________________________________________________________")
                        print(f"Book Number : {i[0]} | Book Title : {i[1]} | <<<Subject Code>>> : {i[2]} | Author : {i[3]} | Publisher : {i[4]} | Price : {i[5]} | Location : {i[6]} " )    
                    
                elif opt == '6':
                    cursor = db.cursor()
                    cursor.execute('SELECT * FROM book')
                    result = cursor.fetchall()
                    print ('\n',cursor.rowcount," Book Search found")
                    # Output
                    for i in result:
                        print ("________________________________________________________________________________________________________________________________________________")
                        print(f"Book Number : {i[0]} | Book Title : {i[1]} | Subject Code : {i[2]} | Author : {i[3]} | Publisher : {i[4]} | Price : {i[5]} | Location : {i[6]} " )   
                       
            else:
                print ("\nIncorrect Option....Try Again")
                search()
                return


# Defining ADD Function
        def add():
            "This Function is to Add Books"
            print ()
            bookNo = int(input("Enter Book Number : "))
            bookTitle = input ("Enter Book Title :  ")
            author = input ("Enter Author Name : ")
            publisher = input ("Enter Publisher : ")
            price = float(input ("Enter the Price : "))
            location = input ("Enter location : ")
            print ("""\nChoose your Subject Name
1) ART - ARTS
2) LIFESTYLE - LIFE
3) ENGLISH - ENG
4) HISTORY - HIS
5) FANTASY - FAN
6) Programming, Business etc - OTHER """)
            
            # Subject Details
            Name = input("Choose your Subject Name : ")
            Name = Name.upper()
            if Name == "ART":
                subjectCode = "ARTS"
            elif Name == "LIFESTYLE":
                subjectCode = "LIFE"
            elif Name == "ENGLISH":
                subjectCode = "ENG"
            elif Name == "HISTORY":
                subjectCode = "HIS"
            elif Name == "FANTASY":
                subjectCode = "FAN"
            else:
                subjectCode = "OTHER"
                                           
            cursor = db.cursor()
            data2 = (bookNo, bookTitle, subjectCode, author, publisher, price, location)
            sql2 = 'INSERT INTO book VALUES(%s, %s, %s, %s, %s, %s, %s)'

            # Process
            cursor.execute(sql2,data2)
            db.commit()
            print () #Chapter Details
            chapter = int(input ("Enter Total chapters "))
            for pg in range (1, chapter+1):
                chapterNo = int(pg)
                title = input(f"Enter the Title for chapter {pg} : ")
                strtPg = int(input(f"Enter Starting page number for chapter {pg} : "))
                endPg = int(input(f"Enter Ending Page number for chapter {pg} : "))
                sql3 = 'INSERT INTO bookchapter VALUES(%s, %s, %s, %s, %s)'
                data = (bookNo, chapterNo,title,strtPg,endPg)
                
                # Process
                cursor.execute(sql3,data)
            db.commit()
            print ()
            print (cursor.rowcount," Book Added Successfully")
            return


# Defining EDIT Function
        def edit():
            "This Function is to update books"
            print ('''Choose an option to edit
1. Book Details
2. Book Chapter Details''')
            print()
            opt = input("Enter the option (1/2) : ")
            print()
            bno = int(input("Enter the Book Number : "))
            if opt == '1':
                print('''You're about to change book details...Choose the detail to edit
1. Title
2. Author
3. Publisher
4. Price
5. Location''')
                opt1 = input("Choose the option (1/2/3/4/5) : ")
                print()
               
                if opt1 == '1':
                    update = input("Type the updated Title information : ")
                    cursor = db.cursor()
                    sql = 'UPDATE book SET Title = %s WHERE BookNO = %s'
                    data = (update, bno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully") 
                
                elif opt1 == '2':
                    update = input("Type the updated Author information : ")
                    cursor = db.cursor()
                    sql = 'UPDATE book SET Author = %s WHERE BookNO = %s'
                    data = (update, bno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully")

                elif opt1 == '3':
                    update = input("Type the updated Publisher information : ")
                    cursor = db.cursor()
                    sql = 'UPDATE book SET Publisher = %s WHERE BookNO = %s'
                    data = (update, bno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully")   
                
                elif opt1 == '4':
                    update = input("Type the updated Price information : ")
                    cursor = db.cursor()
                    sql = 'UPDATE book SET Price = %s WHERE BookNO = %s'
                    data = (update, bno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully")     
                
                elif opt1 == '5':
                    update = input("Type the updated Location information : ")
                    cursor = db.cursor()
                    sql = 'UPDATE book SET Location = %s WHERE BookNO = %s'
                    data = (update, bno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully") 
                    
                else:
                    print ('Please Try Again')
                    edit()
            elif opt == '2':
                print("""You're about to change Chapter detail
1. Chapter Name
2. Starting Page
3. Ending Page""")
                opt2 = input("Enter the option (1/2/3) ")
                if opt2 == "1":
                    chno = input("Enter the Chapter Number")
                    update = input("Type the updated Chapter Title information : ")
                    cursor = db.cursor()
                    sql = 'UPDATE BookChapter SET Title = %s WHERE BookNO = %s AND ChapterNo = %s'
                    data = (update, bno, chno)
                    
                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully") 
                if opt2 == "2":
                    chno = input("Enter the Chapter Number ")
                    update = int(input("Type the updated Starting Page information : "))
                    cursor = db.cursor()
                    sql = 'UPDATE BookChapter SET StartingNo = %s WHERE BookNO = %s AND ChapterNo = %s'
                    data = (update, bno, chno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully") 

                if opt2 == "3":
                    chno = input("Enter the Chapter Number : ")
                    update = int(input("Type the updated Ending Page information : "))
                    cursor = db.cursor()
                    sql = 'UPDATE BookChapter SET  EndingNo = %s WHERE BookNO = %s AND ChapterNo = %s'
                    data = (update, bno, chno)

                    # Process
                    cursor.execute (sql, data)
                    db.commit()
                    print()
                    print (cursor.rowcount," Book Updated Successfully") 
            
            else:
                print ("\nInvalid option to edit. Try Again....")
                edit()
                return


# Defining DLT Function
        def dlt(bno: str):
            "This function is to Delete books" 
            cursor = db.cursor()
            sql1 = 'DELETE FROM bookchapter WHERE BOOKNo = %s'
            data = bno

            # Process
            cursor.execute(sql1,[data])
            db.commit()
            sql2 = 'DELETE FROM book WHERE BookNo = %s'
            cursor.execute(sql2,[data])
            db.commit()
            print()
            print (cursor.rowcount," Book Deleted Successfully") 
            return


# Defining CHAPVIEW Function
        def chapview():
            "This function is to View Chapter"
            print ("Chapter information with Respective Book Numbers")
            cursor = db.cursor()
            cursor.execute('SELECT * FROM bookchapter')
            result = cursor.fetchall()

            # Output
            for i in result:
                print ("_____________________________________________________________________________________________________________________")
                print(f"<<<Book Number>>> : {i[0]} | <<<Chapter No>>> : {i[1]} | Title : {i[2]} | Starting Page No : {i[3]} | Ending Page No : {i[4]} |" )   
            print()
            print ("Note : Chapter View only Available for Testing Purposes with Sample Data")
            print()

            # Read User Input
            bno = int(input("Enter the Book Number : "))
            chno = int(input("Enter the Chapter Number to View : "))

            cursor = db.cursor()
            sql = ('SELECT Title, StartingNo, EndingNo FROM bookchapter WHERE BookNo = %s AND ChapterNo= %s;')
            data = (bno, chno )
            cursor.execute (sql,data)
            result = cursor.fetchall()
            for x in result:
                title = x[0]
                startno = x[1]
                endno= x[2]

            # Reading the Content
            view = fo.readlines()
            time.sleep(1)
            print(f'''\nChapter Title : {title}
Starting Page : {startno}
Ending Page : {endno}''')
            for read in view:
                print(read)
            return

except Error as er:
    print ("Oops!")
    print (er)

# Disconnect from server
db.close

# STOP
