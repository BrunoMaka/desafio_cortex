from tools.tools import Tools
from tools.decorators import *
from .settings import *
from .locators import *
from selenium.webdriver.support.ui import Select
from datetime import datetime
import json,  re


class Crawler(Tools):    
    def get_infos(self, max_collect):
        '''
        Coleta as informações dos processos, coletando no máximo o valor fornecido em max_collect
        '''
        self.max_collect = max_collect
        for doc in DOCS:
            self.print_log(f'INICIANDO - {doc}')
            self.consulta = {
                "input": doc,
                "dataConsulta": datetime.now().strftime('%Y-%m-%d'),
                "processos": []
            }
            Select(self.find(L_SELECT_QUERY_BY)).select_by_visible_text('Documento da Parte')
            self.find(L_INPUT_DOCUMENT).clear()
            self.send_keys_to_element(L_INPUT_DOCUMENT, doc)            
            self.click_in_element(L_BTN_CONSULTAR)           
            while len(self.webdriver.find_elements(*L_NEXT_PAGE)) > 0:
                links = [el.get_attribute('href') for el in self.finds(L_LINKS)] 
                self.open_tab()                 
                self.get_data(links)
                self.close_tab()
                self.click_in_element(L_NEXT_PAGE)
                time.sleep(2)
                if len(self.consulta['processos']) >= int(self.max_collect):
                    break
            json_data = json.dumps(self.consulta)
            with open(f"{doc}-{self.consulta['dataConsulta']}.json", "w") as arquivo:
                arquivo.write(json_data)
            print(f"FINALIZANDO - {doc}")
          
    #@track_processed_items
    def get_data(self, links): 
        '''
        Coleta as informações de cada link
        '''             
        for link in links:                                     
            self.webdriver.get(link) 
            self.click_in_element(L_DADOS_SECUNDARIOS)    
            processo = {
                "uf": self.find(L_INITIALS).text[2:],
                "area": self.format_text(self.find(L_AREA).get_attribute('title')),
                "juiz": self.get_juiz(),
                "partes": self.get_partes(),
                "tribunal": f'{self.find(L_INITIALS).text[:2]}-{self.find(L_INITIALS).text[2:]}',
                "movimentos": self.get_movimentos(),
                "valorCausa": self.get_valor_causa(),
                "assuntosCNJ": self.get_assuntos_CNJ(),
                "urlProcesso": link,
                "grauProcesso": self.get_grau(),
                "orgaoJulgador": self.format_text(self.find(L_VARA).text),
                "unidadeOrigem": self.format_text(self.find(L_FORO).text),
                "classeProcessual": self.get_classe_processual(),
                "dataDistribuicao": self.format_datetime(self.find(L_DATA_DISTRIBUICAO).text),
                "numeroProcessoUnico": self.find(L_NUM_PROCESSO).text.replace('-', '').replace('.', ''),                        
            }      
            self.consulta['processos'].append(processo) 
            self.print_log(f'Finalizando coleta {len(self.consulta["processos"])} de {self.max_collect}') 
            if len(self.consulta['processos']) >= int(self.max_collect):
                break
                        
    def get_juiz(self):
        '''
        Tenta coletar as informações do juiz, caso não encontre, retorna None
        '''
        try: 
            return self.format_text(self.find(L_JUIZ, t=3).get_attribute('title'))
        except:
            return None
        
    def get_part_types(self, type):
        '''
        Tenta coletar as informações do tipo da parte (de acordo com o DE-PARa), caso não encontre, 
        retorna o tipo encontrado formatado de acordo com format_text
        '''
        try:
            return DE_PARA_TIPO[type]
        except:
            return self.format_text(type)        
        
    def get_partes(self):  
        '''
        Coleta as informações da partes
        '''      
        clicked = self.find_element_clickable_and_click(L_EXPANDIR_PARTES)          
        result = []          
        for parte in self.finds(get_parts_loc(clicked)):
            infos_nome = parte.find_elements(By.TAG_NAME, 'td')[1].text.split('\n')
            infos_tipo = parte.find_elements(By.TAG_NAME, 'td')[0].text.strip()            
            partes = {
                "nome": self.format_text(infos_nome[0]),
                "tipo": self.get_part_types(infos_tipo),        
            }           
            if len(infos_nome) > 1:
                partes['advogado'] = []
                for nome in infos_nome[1:]:
                    advogado = {
                        'nome': self.format_text(nome.split(':')[-1]),
                        'tipo': self.format_text(nome.split(':')[0])
                    }
                    partes['advogado'].append(advogado)            
            result.append(partes)
        return result     
    
    def get_movimentos(self):   
        '''
        Coleta as informações das movimentações
        '''     
        clicked = self.find_element_clickable_and_click(L_EXPANDIR_MOVIMENTACOES)                                       
        result = []       
        try:
            for index, movimentacao in enumerate(self.finds(get_movs_loc(clicked), t=5)):                                                
                data = movimentacao.find_elements(By.TAG_NAME, 'td')[0].text
                if data:
                    movimento = movimentacao.find_elements(By.TAG_NAME, 'td')[-1].text.split('\n')
                    m = {
                        'data': self.format_data(data),
                        'indice': len(self.finds(get_movs_loc(clicked))) - index - 1,
                        'titulo': self.format_text(movimento[0])
                    }
                    if len(movimento) > 1:
                        m['descricao'] = self.format_text(movimento[1])
                    result.append(m) 
        except:
            m = {
            'data': None,
            'indice': None,
            'titulo': None
            }
            result.append(m)
        return result 
 
    def get_valor_causa(self):
        '''
        Tenta coletas os valores da causa (caso exista), caso não encontre, 
        retorna um dicionatio com valores None
        '''
        try:
            self.find(L_VALOR, t=3)
            return {
                "moeda": self.find(L_VALOR).text.split(' ')[0],
                "valor": float(self.find(L_VALOR).text.split(' ')[1].replace('.', '').replace(',', '.'))
            }
        except:
            return {
                "moeda": None,
                "valor": None
            }

    def get_assuntos_CNJ(self):
        '''
        Tenta encontrar valores de assunto, caso não encontre, retorna
        um dicionario com None'''
        try:
            return {
                "titulo": self.format_text(self.find(L_ASSUNTO, t=2).text)
            }
        except:
            return {
                "titulo": None
            }

    def get_grau(self):
        ''' Retorna o grau '''
        titulo = self.find(L_GRAU).text
        return int(re.search(r'\d+', titulo).group())
    
    def get_classe_processual(self):
        ''' Retorna a classe processual '''
        return {
            "nome": self.format_text(self.find(L_CLASSE).text)
        }

 