import openpyxl as xl
import logging #logging to store entire process to a file
logging.basicConfig(filename='..//Loggers//Capstone_Project.log',filemode='w',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
from SearchfilesinDrives.Searchfiles import SearchFilesDrives
from Searchindatabase.SearchFilepath import SearchFile
from Searchindatabase.InsertData import InsertFileDB
from CapstoneExceptions.MysqlException import MYSqlError
import mysql.connector #connecting to database
import time #to record time
def searchdata():
    dir=input("Enter the drive like c:// d:// \n")
    filename=input("Enter the filename with extension like demo.txt \n")
    logging.info(f"Drive name{dir} file name{filename}")
    dbobj=SearchFile() #present in searchfilepath
    logging.info(f"class used {SearchFile.__name__}")
    wb=xl.load_workbook("C://testdata//Testfiles.xlsx") #for testing purpose
    ws=wb.active
    try:
        dbobj.Connect("localhost","root","Prabha@23","myhcl",3306)
        logging.info("myhcl database is connected")
        result = dbobj.Search(filename)
    except mysql.connector.Error as err:
        logging.exception(err, exc_info=True)  # created our own exception in Mysqlexceptions
        raise MYSqlError(f'{err.msg}',err.errno)
    finally:
        dbobj.connect.close()
    if len(result)==0:
        print("Not found in database")
        print("Now Searching in Drives..........")
        logging.info("Not found in database")
        logging.info("Now searching in drives")
        start_time=time.time()
        obj=SearchFilesDrives()
        logging.info(f'for searching in drive {SearchFilesDrives.__name__} is used')
        files=obj.searchfiles(dir,filename)
        ws.cell(row=1,column=1).value=str(files)
        wb.save("C://testdata//Testfiles.xlsx") #for testing purpose
        wb.close()
        insertobj = InsertFileDB()
        insertobj.insert(files)
        logging.info(f'files found {files}')
        print(obj.searchfiles(dir,filename))
        print(files)
        obj.start()
        end_time=time.time()
        logging.info(f'time taken{end_time-start_time}')
        logging.info("ending")
        print(end_time-start_time)
    else:
        print("files found")
        print(result)
searchdata()