import mysql.connector
try:
    conn = mysql.connector.connect(host='localhost', user='root', password='', database="tinde")
    mycursor=conn.cursor()

except Exception as e:
    print('could not connect to database')

    

