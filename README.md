
# Como executar o projeto

### 1 Clonar o repositório

```bash```
git clone https://github.com/Lucadavih/projeto-final-de.git
cd projeto-final-de/5.\ Pratica/ProjetoDE

## 2 Criar ambiente virtual
python -m venv .venv

```bash```
source .venv/Scripts/activate

## 3 Instalar dependências

```bash```
pip install -r requirements.txt

## 4 Executar o pipeline
python src/app.py

O pipeline irá:
- Consumir dados da API randomuser.me
- Validar os dados
- Preparar e transformar as informações
- Salvar os dados em um banco SQLite

O banco será criado em:
assets/database.db

## 5 Executar usando tox
O tox cria um ambiente isolado e executa o projeto automaticamente: 

```bash```
tox

Se tudo estiver correto, será aprensentado no terminal:
```congratulations``` :)


## TREE do projeto:

```
ProjetoDE/
│
├── assets/
│   ├── config.yml
│   └── database.db
│
├── src/
│   ├── app.py
│   ├── core.py
│   └── utils.py
│
├── requirements.txt
├── tox.ini
└── README.md
```

---

# Python Course

Repositório destinado ao ensino da linguagem python para iniciantes.

### Conteúdo
---
0. Dados: datasets utilizados ao longo do curso
1. Fundamentos 
    - Estruturas Fundamentais
    - Paths e leitura de arquivos
    - Funções 
2. Sources
    - API com Flask
    - Sqlite e SqlAnchemy
    - ChromaDB
    - Requests
3. Manipulação de Dados
    - Numpy
    - Pandas
    - Análise de Dados
4. Projeto: ML Models
    - Sklearn
    - Pydantic
    - Streamlit
5. Prática

### Setup Projetos
---
1. Ambiente virtual
```
python -m venv env 
source env/bin/activate
## Windows
>> python -m venv env 
>> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
>> .\env\Scripts\Activate.ps1 
```

2. Requirements
```
## Para gerar o arquivo de dependências
>> pip freeze >> requirements.txt
## Para instalar os pacotes
>> pip install -r requirements.txt 
```

3. Criação do PYTHONPATH na raiz do projeto
```
>> export PYTHONPATH=$PYTHONPATH:./
## For Windows
>> $env:PYTHONPATH = "$env:PYTHONPATH;$(Get-Location)"
```

### Referências
---
1. https://python-guide-pt-br.readthedocs.io/pt-br/latest/
2. https://greenteapress.com/thinkpython/html/index.html
3. https://www.hackerrank.com/
4. https://peps.python.org/pep-0008/

### Links Úteis
---
1. https://www.anaconda.com/download
2. https://git-scm.com/install/windows
3. https://code.visualstudio.com/download
