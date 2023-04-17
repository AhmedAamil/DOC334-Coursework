
# START

# Importing Modules and Packages
import mysql.connector
import time
import dbms
### import sys

# Initializing Variables (Global etc.)
option = ''
answer = ''
fo = 0

# Opening a .TXT file
fo = open('ChapterView.txt','r+')

# Input & Process
print ("\n\t\tWELCOME TO ABC BOOK STORE LIBRARY SYSTEM")

# Defining MENU Function for the Console Interface
def menu():
    "console interface"
    print("———————————————————————————————————————")
    print('''1. SEARCH Book
2. ADD Book
3. EDIT Book
4. DELETE Book
5. Book CHAPTER VIEW
6. EXIT''')
    print("———————————————————————————————————————")

    # Read User Input
    option = input("\nEnter Requested Option (1/2/3/4/5) : ") 

    #Process
    print()
    if option == '1':
        dbms.search()
    elif option == '2':
        dbms.add()
    elif option == '3': 
        dbms.edit()
    elif option == '4':
        bNumber = input("Enter the Book Number : ")
        dbms.dlt(bNumber)
    elif option == '5':
        dbms.chapview()
    elif option == '6':
        print ("You're about to exit.") 
    else:
        print ("\n\nOops!, Wrong Option....Please try again")
        menu()

# Output    
# Calling the MENU
menu()

while True:
    print()
    answer = input("Do You want to EXIT the System ? (YES or NO) ")
    answer = answer.upper()
    
    if answer == 'YES':
        print()   
        time.sleep(1)
        print ("Thanks For using ABC Book Store.")
        break
    elif answer == 'NO':
        print ("\n\t\tWELCOME BACK TO ABC BOOK STORE LIBRARY SYSTEM")
        menu()
        # User Input Validation
    else:
        print ("\n<<INVALID USER INPUT>>")
        print()
        answer = input("Do You want to EXIT the System ? (YES or NO) ")
        
# Disconnection(s)
fo.close()

# STOP
