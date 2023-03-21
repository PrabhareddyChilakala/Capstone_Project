from Searchindatabase.DBConnection import DatabaseConnection
class InsertFileDB(DatabaseConnection):
    def __init__(self):
        self.dbconnect=self.Connect("localhost","root","Prabha@23","myhcl",3306)
    def insert(self,files):
        self.files=files
        self.insertcur = self.connect.cursor()
        for f in self.files:
            sql="insert into fileinfo(filename) values(%s)"
            self.insertcur.execute(sql,(f,))
            self.connect.commit() #storing permanent changes to DB
        print("Files added successfully")

