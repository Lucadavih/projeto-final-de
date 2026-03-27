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
├── README.md
├── requirements.txt
└── tox.ini
```

---
