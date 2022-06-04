import mysql.connector
import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     database='pythontest')
        query='create table if not exists user(userId INT PRIMARY KEY,username VARCHAR(200), phone VARCHAR(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print('created object')

    #Insert
    def insert_user(self,userid,username,phone):
        query='insert into user(userid,username,phone) values({},"{}","{}")'.format(userid,username,phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('user saved to db')
    #Fetch all
    def fetch_all(self):
        query='select * from user'
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print('User Id : ', row[0])
            print('User Name : ', row[1])
            print('phone : ', row[2])
            print()
            print()

    #delete
    def delete_user(self, userid):
        query = 'delete from user where userid={}'.format(userid)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print('deleted')

    #update
    def update_user(self,userid,newName,newPhone):
        query = 'update user set userName="{}",phone="{}" WHERE userid={}'.format(newName,newPhone,userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print('Updated')


helper = DBHelper()
helper.fetch_all()