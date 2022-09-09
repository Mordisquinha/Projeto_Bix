import os
import requests 
import pandas as pd
from funcoes_db import Connect_db

conexao = Connect_db()
db = conexao.db

def download_parquet():
    link = 'https://storage.googleapis.com/challenge_junior/categoria.parquet'
    response = requests.get(link)
    open('categoria.parquet', 'wb').write(response.content)
    print('Arquivo: categoria.parquet baixado.')
    return response
if __name__ == '__main__':
    if download_parquet():
        parquet = pd.read_parquet('categoria.parquet', engine='pyarrow')
        df = parquet.rename({'id':'id_categoria', 'nome_categoria':'categoria'}, axis=1)
        conexao.truncate_categorias()
        df.to_sql('categorias', con=conexao.engine, if_exists='append', index=False)

    else:
        print('Não foi possível baixar o arquivo .parquet')

    os.remove('./categoria.parquet')
    print('Arquivo: categoria.parquet deletado.')
    print('Fim da etapa parquet'.center(100, '-'))