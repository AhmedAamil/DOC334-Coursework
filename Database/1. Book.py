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
        # Execute SQL query
        cursor.execute ("""CREATE TABLE IF NOT EXISTS Book
                        (BookNo int(50) NOT NULL,
                         Title varchar(150),
                         SubjectCode varchar(60),
                         Author varchar(40),
                         Publisher varchar(50),
                         Price float(25),
                         Location varchar(50),
                         PRIMARY KEY(BookNo));""")
        data = cursor.fetchall()      
        
except Error as e:
    print ("Oops!")
    print (e)

# Disconnect from server
db.close