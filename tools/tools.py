from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup
from unidecode import unidecode
from datetime import datetime
import logging, os
from abc import ABC
from crawler.settings import *


class Tools(ABC):   
    def __init__(self, webdriver, url):       
        self.webdriver = webdriver       
        self.webdriver.maximize_window()        
        self.url = url    
        self.setup_log()  

    def print_log(self, msg):
        print(msg)
        logging.info(msg)  

    def setup_log(self):
        logging.basicConfig(
        filename =  os.getcwd() + "\\" + f"{CRAWLER_NAME}.log", 
        level = logging.INFO, 
        filemode='w', 
        encoding='utf8',
        format = "%(asctime)s :: %(message)s",
        datefmt = '%d-%m-%Y %H:%M:%S') 

    def wait_(self, t=60):
        return WebDriverWait(self.webdriver, t)
        
    def wait_element(self, locator, t=60, el_type='presence'):        
        if el_type == 'presence':
            return self.wait_(t).until(EC.presence_of_element_located(locator))
        elif el_type == 'clickable':
            return self.wait_(t).until(EC.element_to_be_clickable(locator))
        elif el_type == 'visibility':
            return self.wait_(t).until(EC.visibility_of_element_located(locator))
    
    def find(self, locator, t=60, el_type='presence'):        
        self.wait_element(locator, t, el_type)
        return self.webdriver.find_element(*locator)
    
    def finds(self, locator, t=60, el_type='presence'):        
        self.wait_element(locator, t, el_type)
        return self.webdriver.find_elements(*locator)    
        
    def open_url(self):        
        self.webdriver.get(self.url)

    def open_tab(self):
        self.webdriver.execute_script("window.open('', '_blank');")
        self.webdriver.switch_to.window(self.webdriver.window_handles[-1])
    
    def close_tab(self):
        self.webdriver.close()
        self.webdriver.switch_to.window(self.webdriver.window_handles[-1])

    def click_in_element(self, locator, t=60, el_type='presence'):        
        self.find(locator, t, el_type).click()    
    
    def click_in_elements(self, locator, i, t=60, el_type='presence'):        
        elements = self.finds(locator, t, el_type)
        elements[i].click()

    def send_keys_to_element(self, locator, keys, t=60, el_type='presence'):        
        self.find(locator, t, el_type).send_keys(keys)

    def send_keys_to_elements(self, locator, i, keys, t=60, el_type='presence'):        
        elements = self.finds(locator, t, el_type)
        elements[i].send_keys(keys)
     
    def switch_to_frame(self, to):        
        return self.webdriver.switch_to.frame(to)
    
    def switch_to_default_content(self):        
        return self.webdriver.switch_to.default_content()

    def switch_to_parent_frame(self):       
        return self.webdriver.switch_to.parent_frame()

    def scroll(self, pixels=300, to='DOWN'):
        if to == 'DOWN':
            self.webdriver.execute_script(f"window.scrollBy(0, {pixels});")
        elif to == 'UP':
            self.webdriver.execute_script(f"window.scrollBy(0, {-pixels});")
        
    def find_element_clickable_and_click(self, locator):        
        self.clicked = False
        while not self.clicked:
            try:
                self.click_in_element(locator, t=1) 
                self.clicked = True
                return self.clicked 
            except ElementClickInterceptedException as err:              
                self.scroll()
            except:
                self.clicked = True
                return False
        


    def format_text(self, text):
        if text:
            return unidecode(text).upper().strip().replace('\n', '').replace('\t', '')
    
    def format_data(self, data_str):
        return datetime.strptime(data_str, "%d/%m/%Y").strftime("%Y-%m-%dT00:00:00")
    
    def format_datetime(self, datetime_str):
        datetime_str = datetime_str.split('-')[0].strip()
        return datetime.strptime(datetime_str, "%d/%m/%Y às %H:%M").strftime("%Y-%m-%dT%H:%M:%S")
    
    def split_text(self, text):        
        return [unidecode(texto.strip().upper()) for texto in text.split('\n') if texto.strip()]
    
    
    def split_list(self, list, num):              
        splited_list = []
        a = int(len(list) / num)
        len_l = len(list)
        for i in range(a):
            start = int(i*len_l/a)
            end = int((i+1)*len_l/a)
            splited_list.append(list[start:end])
        return splited_list
    
    def create_list(self, tag):        
        req = self.webdriver.page_source
        soup = BeautifulSoup(req, 'html.parser')
        tags = soup.find_all(tag)
        lista = []
        for t in tags:
            lista.append(t.text.strip())
            lista = list(filter(('').__ne__, lista))
        return lista
    
   