import mysql.connector #to connect with database
from CapstoneExceptions.MysqlException import MYSqlError
class DatabaseConnection():
    def Connect(self,localhost,username,password,database,port): #127.0.0.1-loop back address,port num of mysql is:3306
        self.host=localhost
        self.username=username
        self.password=password
        self.database=database
        self.port=port
        self.connect=mysql.connector.Connect(host=self.host,username=self.username,password=self.password,database=self.database,port=self.port)
        self.cur=self.connect.cursor() #"cursor" is used to execute sql commands,"connect" is used to connect with database
