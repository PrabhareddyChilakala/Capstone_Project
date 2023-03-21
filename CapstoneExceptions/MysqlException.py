import mysql.connector
class MYSqlError(Exception):
    def __init__(self,message,errno):
        super().__init__(message) #message will be send to super class
        self.err_number=errno