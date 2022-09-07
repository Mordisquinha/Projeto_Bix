import requests 
import database as database
import pandas as pd
import os
from database import Session


db = Session()

def download_parquet():
    link = 'https://storage.googleapis.com/challenge_junior/categoria.parquet'

    response = requests.get(link)
    open('categoria.parquet', 'wb').write(response.content)

    return 'Arquivo: categoria.parquet baixado.'

paquet = download_parquet()
print(paquet)
if paquet:
    parquet = pd.read_parquet('categoria.parquet', engine='pyarrow')

    df = parquet.rename({'id':'id_categoria', 'nome_categoria':'categoria'}, axis=1)

    db.execute('SET FOREIGN_KEY_CHECKS = 0;')
    db.execute('truncate categorias;')
    db.execute('SET FOREIGN_KEY_CHECKS = 1')

    df.to_sql('categorias', con=database.engine, if_exists='append', index=False)

else:
    print('Não foi possível baixar o arquivo .parquet')

os.remove('./categoria.parquet')
print('Arquivo: categoria.parquet deletado.')
print('Fim da etapa api'.center(100, '-'))