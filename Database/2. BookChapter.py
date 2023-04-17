import mysql.connector
from mysql.connector import Error
# Open database connection
conDict = {"host":"localhost",
          "database": "library",
          "user":"root",
          "password":""}

try:
    db = mysql.connector.connect (**conDict)
    if db.is_connected():
        cursor = db.cursor()
        # Execute SQL query to Create Chapter Table
        cursor.execute ("""CREATE TABLE IF NOT EXISTS BookChapter
                        (BookNo int(50), ChapterNo int(40), Title varchar (250), StartingNo int(50), EndingNo int(50),
                        PRIMARY KEY(BookNo,ChapterNo),
                        FOREIGN KEY(BookNo) REFERENCES Book(BookNo));""")
        data = cursor.fetchall()                
        
except Error as e:
    print ("Oops!")
    print (e)

# Disconnect from server
db.close