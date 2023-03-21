import os
import threading #threading is used for I/O bound operations
class SearchFilesDrives(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self) #for initialise the thread class, instead of threading we also use super() keyword
        self.path=[] #to store path
    def searchfiles(self,drives,filename):
        self.drive=drives
        self.filename=filename
        for root,dir,files in os.walk(self.drive): #recursively goes through the directories
            for f in files:
                if f==self.filename:
                    self.path.append(os.path.abspath(root)+filename) #abspath means to get the absolute path
        return self.path
    def run(self)->None:
        self.searchfiles(self.drive,self.filename)
