from tkinter import *



import mysql.connector

class Login:

    def __init__(self):


        self.conn=mysql.connector.connect(host='localhost',user='root',password='',database="tinder2")

        self.mycursor=self.conn.cursor()

        self.root=Tk()



        self.root.title('login')
        self.root.configure(background="black")
        canvas= Canvas(self.root,width=950,height=500)
        canvas.pack()





        my_image = PhotoImage(file="C:\\Users\\sam's\\Documents\\Tinderp.gif")
        canvas.create_image(0,0,anchor=NW, image=my_image)




        self.root.minsize(900,1050)
        self.root.maxsize(900,1050)


        self.email_label=Label(self.root,text='Enter Email',fg='white',bg='black')
        self.email_label.pack()

        self.email_input=Entry(self.root)
        self.email_input.pack()

        self.password_label=Label(self.root,text='Enter Password',fg='white',bg='black')
        self.password_label.pack()

        self.password_input=Entry(self.root)
        self.password_input.pack()

        self.button=Button(self.root,text='login',fg='blue',bg='white',command=lambda :self.perform())
        self.button.pack()

        self.result=Label(self.root,text='',fg='red')
        self.result.pack()

        self.buttonA=Button(self.root,text='Not a user?create new account',fg='black',command=lambda :self.dhaka())
        self.buttonA.pack()

        self.root.mainloop()





    def perform(self):

        email=self.email_input.get()
        password=self.password_input.get()

        self.mycursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND 
                               `password` LIKE '{}'""".format(email,password))
        user_list=self.mycursor.fetchall()

        if len(user_list)>0:
            self.result.configure(text='WELCOME')
        else:
            self.result.configure(text='incorrect')




    def dhaka(self):




        self.rootA=Tk()
        self.rootA.title('register')

        self.rootA.configure(background="black")





        self.rootA.minsize(350,550)
        self.rootA.maxsize(350,550)

        self.name_label= Label(self.rootA, text='Enter Name', fg='white', bg='black')
        self.name_label.pack()

        self.name_input = Entry(self.rootA)
        self.name_input.pack()

        self.email_reg_label = Label(self.rootA, text='Enter Email', fg='white', bg='black')
        self.email_reg_label.pack()

        self.email_reg_input = Entry(self.rootA)
        self.email_reg_input.pack()

        self.password_reg_label = Label(self.rootA, text='Enter Password', fg='white', bg='black')
        self.password_reg_label.pack()

        self.password_reg_input = Entry(self.rootA)
        self.password_reg_input.pack()

        self.gender_label = Label(self.rootA, text='Enter Gender', fg='white', bg='black')
        self.gender_label.pack()
        self.gender_input = Entry(self.rootA)
        self.gender_input.pack()

        self.age_label = Label(self.rootA, text='Enter age', fg='white', bg='black')
        self.age_label.pack()

        self.age_input = Entry(self.rootA)
        self.age_input.pack()


        self.city_label = Label(self.rootA, text='Enter City', fg='white', bg='black')
        self.city_label.pack()
        self.city_input = Entry(self.rootA)
        self.city_input.pack()

        self.button3 = Button(self.rootA, text='login', fg='blue', bg='white', command=lambda: self.perform_reg())
        self.button3.pack()

        self.result1 = Label(self.rootA, text='', fg='red')
        self.result1.pack()

        self.rootA.mainloop()
    def perform_reg(self):
        name = self.name_input.get()
        email_reg = self.email_reg_input.get()
        password_reg = self.password_reg_input.get()
        gender =self.gender_input.get()
        age = self.age_input.get()
        city = self.city_input.get()

        self.mycursor.execute("""INSERT INTO `users` 
               (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`) VALUES (NULL,'{}','{}','{}','{}','{}','{}')
               """.format(name, email_reg, password_reg, gender, age, city))
        self.conn.commit()
    

        self.result1.configure(text='REGISTRATION SUCCESSFUL')
















Object = Login()