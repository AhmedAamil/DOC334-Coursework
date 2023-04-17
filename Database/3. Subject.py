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
        # Execute SQL query to Create Subject Table
        cursor = db.cursor()
        cursor.execute ("""CREATE TABLE IF NOT EXISTS Subject
                        (SubjectCode Varchar(60)NOT NULL, Name varchar(70) NOT NULL,
                        PRIMARY KEY(SubjectCode));""")
        data = cursor.fetchall()

        # Execute Subject Details
        sql = '''INSERT INTO subject (SubjectCode, Name) VALUES
('ARTS', 'ART'),
('ENG', 'ENGLISH'),
('FAN', 'FANTASY'),
('HIS', 'HISTORY'),
('LIFE', 'LIFESTYLE');'''
        cursor.execute(sql)
        db.commit()
        
except Error as e:
    print ("Oops!")
    print (e)


# Disconnect from server
db.close
