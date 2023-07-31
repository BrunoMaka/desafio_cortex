from tools.check_working import CheckWorking
import time, logging

def track_processed_items(func):
    '''
    Processar itens de um dicionário e após concluído, não repetir mesmo item
    NÃO UTILIZADO NO MOMENTO
    '''
    processed_items = set()
    def wrapper(self, dictionary):
        for key, value in dictionary.items():
            if key not in processed_items:      
                func(self, {key: value})
                processed_items.add(key)      
    return wrapper

def check_free(cls): 
    '''
    Verifica se já há uma instância do Crawler rodando
    NÃO UTILIZADO NO MOMENTO
    '''   
    def before_after_init(*args, **kwargs):     
        CheckWorking().check_free()
        instance = cls(*args, **kwargs)
        CheckWorking().delete_lock_file()
        return instance
    return before_after_init

def measure_execution_time(funcao):
    '''
    Mede o tempo de execussão de uma função
    '''
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funcao(*args, **kwargs)
        end = time.time()
        time_executed = end - start
        print_log(f"A função {funcao.__name__} levou {round(time_executed, 2)} segundos (cerca de {int(time_executed/60)} minuto(s)) para ser executada.")
        return result
    return wrapper

def print_log(msg):
    '''
    Escreve uma mensagem no .log
    '''
    print(msg)
    logging.info(msg)  