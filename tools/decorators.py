from tools.check_working import CheckWorking
import time

def track_processed_items(func):
    '''
    Processar itens de um dicionário e após concluído, não repetir mesmo item
    '''
    processed_items = set()
    def wrapper(self, list):
        for item in list:
            if item not in processed_items:      
                func(self, item)
                processed_items.add(item)      
    return wrapper

def check_free(cls): 
    '''
    Verifica se já há uma instância do Crawler rodando
    '''   
    def before_after_init(*args, **kwargs):     
        CheckWorking().check_free()
        instance = cls(*args, **kwargs)
        CheckWorking().delete_lock_file()
        return instance
    return before_after_init

def measure_execution_time(funcao):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funcao(*args, **kwargs)
        end = time.time()
        time_executed = end - start
        print(f"A função {funcao.__name__} levou {time_executed} segundos para ser executada.")
        return result
    return wrapper