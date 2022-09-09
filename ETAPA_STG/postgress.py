import pandas as pd
from funcoes_db import Connect_db

conexao = Connect_db()
db = conexao.db
conn = conexao.consultar_db(conexao.select_venda)

if __name__ == '__main__':
    if conn:
        df = pd.DataFrame(conn, columns=['id_venda', 'id_funcionario', 'id_categoria', 'data_venda', 'venda'])
        conexao.truncate_vendas()
        df.to_sql('vendas', con=conexao.engine, if_exists='append', index=False)

    else:
        print('Não foi possível conectar ao banco de dados postgresql')

    print('Fim da etapa postgress'.center(100, '-'))