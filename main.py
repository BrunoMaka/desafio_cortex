
from selenium.webdriver import Chrome
from crawler.crawler import Crawler
from crawler.settings import *
from tools.webdriver_setup import Setup
from tools.decorators import *
import os

#@check_free
class Application():
    def __init__(self):       
        self.run()

    @measure_execution_time
    def run(self):        
        setup = Setup(os.getcwd())       
        self.webdriver = Chrome(service=setup.s, options=setup.opt)
        self.crawler = Crawler(self.webdriver, MAIN_URL)        
        self.crawler.open_url()        
        self.crawler.get_infos(MAX_COLLECT)

if __name__ == "__main__":
    Application()