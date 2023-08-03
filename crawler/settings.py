import sys

# URL PRINCIPAL
MAIN_URL = 'https://esaj.tjsp.jus.br/cpopg/open.do'

# NOME DO CRAWLER
CRAWLER_NAME = 'crawler_desafio_cortex'

# MAXIMO DE COLETAS DESEJADAS
try:
    MAX_COLLECT = sys.argv[1]
except:
    MAX_COLLECT = 5

# DOCUMENTOS A SEREM COLETADOS
DOCS = [
    '60746948000112',
    '60701190000104'
]

# DE-PARA DO TIPO DA PARTE
DE_PARA_TIPO = {
    'Reqte': 'REQUERENTE',
    'Reqdo': 'REQUERIDO',
    'Reqda': 'REQUERIDA',
    'Perito': 'PERITO',
    'Imptte': 'IMPTTE',
    'Imptdo': 'IMPTDO',
    'Imptda': 'IMPTDA',
    'Interesda.':'INTERESSADA',
    'Interesdo.':'INTERESSADO',
    'Embargte':'EMBARGANTE',
    'Embargdo': 'EMBARGADO',
    'Advogado': 'ADVOGADO',
    'Advogada': 'ADVOGADA',
    'DenunLide': 'DENUNCICAO DA LIDE',
    'Ministério Pub': 'MINISTRARIO PUBLICO',
    'TerIntCer': 'TERINTCER',
    'Adm-Terc.': 'ADM-TERCEIRO',
    'LitisPas': 'LITISPAS',
    'Herdeiro': 'HERDEIRO',
    'Herdeira': 'HERDEIRA',
    'LitisAtiv.': 'LITIS ATIV',
    'Exeqte': 'EXECUTANTE',
    'Exectdo': 'EXECUTADO',
    'Exectda': 'EXECUTADA',
    'Reclamante': 'RECLAMANTE',
    'Reclamado': 'RECLAMADO',
    'Reclamada': 'RECLAMADA',
    'Autor': 'AUTOR',
    'Soc. Adv - Req': 'SOC. ADV. REQ.',
    'Litisconsorte':'LITISCONSORTE',
    'Credor': 'CREDOR',
    'PromotTer': 'PROMOTOR TERCEIRO',
    'Réu': 'REU',
    'Confte': 'CONFTE'
}