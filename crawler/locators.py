from selenium.webdriver.common.by import By

L_SELECT_QUERY_BY = (By.ID, 'cbPesquisa')
L_INPUT_DOCUMENT = (By.ID, 'campo_DOCPARTE')
L_BTN_CONSULTAR = (By.ID, 'botaoConsultarProcessos')
L_NEXT_PAGE = (By.CSS_SELECTOR, 'a[title="Próxima página"]')
L_LINKS = (By.CLASS_NAME, 'linkProcesso')
L_INITIALS = (By.CLASS_NAME, 'header__navbar__brand__initials')
L_DADOS_SECUNDARIOS = (By.ID, 'botaoExpandirDadosSecundarios')
L_EXPANDIR_PARTES = (By.ID, 'setasDireitapartes')
L_EXPANDIR_MOVIMENTACOES = (By.ID, 'setasDireitamovimentacoes')
L_AREA = (By.CSS_SELECTOR, '#areaProcesso span')
L_JUIZ = (By.CSS_SELECTOR, '#juizProcesso')
L_VALOR = (By.ID, 'valorAcaoProcesso')
L_ASSUNTO = (By.ID, 'assuntoProcesso')
L_GRAU = (By.CLASS_NAME, 'header__navbar__title')
L_VARA = (By.ID, 'varaProcesso')
L_FORO = (By.ID, 'foroProcesso')
L_CLASSE = (By.ID, 'classeProcesso')
L_DATA_DISTRIBUICAO = (By.ID, 'dataHoraDistribuicaoProcesso')
L_NUM_PROCESSO = (By.ID, 'numeroProcesso')

def get_parts_loc(clicked):
    ''' Retorna o locator da tabela de partes do elemento, de acordo com o clique feito ou não'''
    if clicked:
        return (By.CSS_SELECTOR, '#tableTodasPartes tr')
    else:
        return(By.CSS_SELECTOR, '#tablePartesPrincipais tr')
    
def get_movs_loc(clicked):
    ''' Retorna o locator da tabela de movimentações do elemento, de acordo com o clique feito ou não'''
    if clicked:
        return (By.CSS_SELECTOR, '#tabelaTodasMovimentacoes tr')
    else:
        return(By.CSS_SELECTOR, '#tableMovimentacoesPrincipais tr')

