import psycopg2
import pandas as pd
import database
from database import Session


db = Session()

def conecta_db():
  conexao = psycopg2.connect(host='34.173.103.16', 
                         database='postgres',
                         user='junior', 
                         password='|?7LXmg+FWL&,2(')
  return conexao


def consultar_db(sql):
  conexao = conecta_db()
  cursor = conexao.cursor()
  cursor.execute(sql)
  resultado = cursor.fetchall()
  registros = []
  for rec in resultado:
    registros.append(rec)
  conexao.close()
  return registros


sql = """SELECT * FROM public.venda"""
conn = consultar_db(sql)
if conn:
    df = pd.DataFrame(conn, columns=['id_venda', 'id_funcionario', 'id_categoria', 'data_venda', 'venda'])

    db.execute('SET FOREIGN_KEY_CHECKS = 0;')
    db.execute('truncate vendas;')
    db.execute('SET FOREIGN_KEY_CHECKS = 1')

    df.to_sql('vendas', con=database.engine, if_exists='append', index=False)
else:
    print('Não foi possível conectar ao banco de dados postgresql')

print('Fim da etapa postgress'.center(100, '-'))