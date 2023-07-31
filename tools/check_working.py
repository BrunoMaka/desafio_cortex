import os

class CheckWorking():
    '''
    Veririfica se há outra instância do crawler
    '''
    def __init__(self):   
        self.path = os.getcwd()       
        try:
            os.mkdir(self.path + '\\tmp')
        except:
            pass
        self.LOCK_FILE = "\\tmp\\program.lock"   
    
    def check_free(self):
        '''
        Verifica se o crawler está livre. 
        Em caso posotovo, um arquivo .lock é criado para impedir a criação de outra instância do crawler
        '''
        if not os.path.exists(self.path + self.LOCK_FILE):
            self.create_lock_file()
        else:
            raise Exception("Crawler working. Please wait!!")

    def create_lock_file(self):  
        '''
        Cria o arquivo .lock
        '''  
        open(self.path + self.LOCK_FILE, 'w').close()

    def delete_lock_file(self): 
        '''
        Deleta o arquivo .lock apos a conclusão
        ''' 
        try:    
            os.remove(self.path + self.LOCK_FILE)   
        except:
            pass   