import pandas as pd
import requests
import utils as utils

import pandas as pd
import requests
import sqlite3
import re


def ingestion(configs):
    """
    Função de ingestão dos dados.
    Consome dados da API https://randomuser.me
    Retorna um DataFrame pandas.
    """

    url = "https://randomuser.me/api/"

    params = {
        "results": 10  # mínimo exigido
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception("Erro ao consumir API")

    data = response.json()["results"]

    # transforma JSON em dataframe
    df = pd.json_normalize(data)

    return df


def validation_inputs(df, configs):
    """
    Função de validação dos dados antes de salvar no banco de dados
    Output: Se não estiver no padrão correto interrompe o processo e salva alerta em 
    um arquivo de logs. Se estiver correto, salva log com mensagem: 'Dados corretos'
    """
    return True


def preparation(df, configs):
    """
    Função de preparação dos dados:
        - Renomeia colunas
        - Ajusta tipo dos dados
        - Remove caracter especial
        - Salva em SQLite (assets/)
    """

    # ---------- Renomear colunas ----------
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
    conn = sqlite3.connect("assets/database.db")

    df.to_sql(
        "users",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    return True

