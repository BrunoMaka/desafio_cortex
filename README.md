# Crawler - Processos Judiciais - TJ-SP

Este é um projeto desenvolvido em Python, para coletar os dados dos Processos Judiciais do TJ-SP.

## Configurações iniciais

Faça o clone do projeto https://github.com/BrunoMaka/desafio_cortex.git

### Instalação local

Recomenda-se a instalação das dependências do projeto em um ambiente virtual. Siga os passos abaixo:

1. Dentro da raiz do projeto, crie um ambiente virtual:
```
python3 -m venv venv
```

2. Ative o ambiente virtual:
- No Linux/Mac:
  ```
  source venv/bin/activate
  ```
- No Windows:
  ```
  venv\Scripts\activate
  ```

3. Instale as dependências do projeto:
```
pip install -r requirements.txt
```

4. Eexecute o comando:

```
python main.py max_collect
```

onde ```max_collect``` é o número maximo de coletas de processos que deseja. Caso este número seja omitido, o padrão é de 5 coletas



