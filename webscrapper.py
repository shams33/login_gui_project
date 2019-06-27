import requests
import mysql.connector



from bs4 import BeautifulSoup

conn=mysql.connector.connect(host='localhost',user='root',password='',Database='tinder2')
mycursor=conn.cursor()

r=requests.get("http://nfly.in/internship/browse")
soup=BeautifulSoup(r.content,'html.parser')

for i in soup.find_all('a'):
    print(i.text)
    mycursor.execute("""INSERT INTO `users` 
        (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')
        """.format(name,email,password,gender,age,city))
    conn.commit()
    print('complete')

