# create a class to hold the sql query
import mysql.connector
import os
HOST =os.getenv('HOST')
USERDB = os.getenv('USERDB')
PASSWORD = os.getenv('PASSWORD')
PORT=os.getenv('PORT')
DATABASE= os.getenv('DATABASE')
class DbConnection():
    def __init__ (self):
        self.connection = mysql.connector.connect(host=HOST, 
                                port=PORT, 
                                user=USERDB, 
                                password=PASSWORD, 
                                database=DATABASE)
        self.cursor = self.connection.cursor(buffered=True)

    def getUserId(self, userid):
        sql = 'SELECT * FROM `member` WHERE `username` = %s'
        id = (userid,)
        self.cursor.execute(sql, id)
        result = self.cursor.fetchone()
        return result


    def addUser(self, username, userid, password):
        sql = 'INSERT INTO `member` (`name`,`username`,`password`) VALUES(%s, %s, %s)'
        val = (f'{username}',f'{userid}',f'{password}')
        self.cursor.execute(sql, val)
        self.connection.commit()
        return

    def verifyUser(self,userid):
        sql = 'SELECT `name`,`username`, `password` from `member` WHERE `username` = %s'
        id = (userid,)
        self.cursor.execute(sql,id)
        result = self.cursor.fetchone()
        return result


    def connectionClose(self):
        try:
            self.cursor.close()
            self.connection.close()
        except:
            print("The connection is not yet closed")
        else:
            print("The connection is closed")
            return 
