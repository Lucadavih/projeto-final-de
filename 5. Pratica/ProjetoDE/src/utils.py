import pandas as pd
import requests
import logging
import sqlite3
import re


def ingestion(configs):
    """
    Função de ingestão dos dados.
    Consome dados da API https://randomuser.me
    Retorna um DataFrame pandas.
    """
    #buscando do arquivo config
    url = configs["api"]["url"]


    params = {
         "results": configs["api"]["results"]
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()["results"]

    # transforma JSON em dataframe
    df = pd.json_normalize(data)

    return df




def validation_inputs(df, configs):
    """
    Valida dados antes de salvar no banco.
    """

    logging.info("Iniciando validação dos dados")

    # valida dataframe vazio
    if df.empty:
        logging.error("DataFrame vazio")
        raise ValueError("DataFrame vazio")

    # valida número mínimo de linhas
    min_rows = configs["validation"]["min_rows"]
    if len(df) < min_rows:
        logging.error("Quantidade de linhas insuficiente")
        raise ValueError("Poucas linhas")

    # valida colunas obrigatórias
    required_cols = configs["validation"]["required_columns"]

    for col in required_cols:
        if col not in df.columns:
            logging.error(f"Coluna ausente: {col}")
            raise ValueError(f"Coluna ausente: {col}")

    logging.info("Dados corretos")

    return True


def preparation(df, configs):
    
    """
    Função de preparação dos dados:
        - Renomeia colunas
        - Ajusta tipo dos dados
        - Remove caracter especial
        - Salva em SQLite (assets/)
    """
    # ---------- validação dos inputs ----------
    validation_inputs(df, configs)
    
    # ---------- Renomear colunas ----------
    logging.info("Iniciando preparação dos dados")
    
    df = df.rename(columns={
        "name.first": "first_name",
        "name.last": "last_name",
        "dob.age": "age"
    })

    # ---------- Ajustar tipos ----------
    if "age" in df.columns:
        df["age"] = df["age"].astype(int)

    # ---------- Remover caracteres especiais ----------
    df.columns = [
        re.sub(r"[^a-zA-Z0-9_]", "", col)
        for col in df.columns
    ]

    # ---------- Salvar SQLite ----------
    db_path = configs["database"]["path"]
    table_name = configs["database"]["table"]

   with sqlite3.connect(db_path) as conn:
    df.to_sql(
        table_name,
        conn,
        if_exists="replace",
        index=False
    )
    
    logging.info("Dados salvos com sucesso no SQLite")
    return True

