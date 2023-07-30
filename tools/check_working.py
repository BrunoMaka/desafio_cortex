import os

class CheckWorking():
    def __init__(self):   
        self.path = os.getcwd()       
        try:
            os.mkdir(self.path + '\\tmp')
        except:
            pass
        self.LOCK_FILE = "\\tmp\\program.lock"   
    
    def check_free(self):
        if not os.path.exists(self.path + self.LOCK_FILE):
            self.create_lock_file()
        else:
            raise Exception("Crawler working. Please wait!!")

    def create_lock_file(self):    
        open(self.path + self.LOCK_FILE, 'w').close()

    def delete_lock_file(self):  
        try:    
            os.remove(self.path + self.LOCK_FILE)   
        except:
            pass   