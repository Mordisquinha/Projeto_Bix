import pymysql.cursors 



def conecta_db():
  conexao = pymysql.connect(host='mysqlpessoal.chfthweo9mu0.us-west-2.rds.amazonaws.com',
                            user='gsantiago',
                            password='11235813',
                            database='rel',
                            cursorclass=pymysql.cursors.DictCursor)
  return conexao

a = conecta_db()
print(a)

def insert_db(sql):
    with sql as s:
        script = s.read().replace('\n', ' ')

    conexao = conecta_db()
    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute(script)
        conexao.commit()
    return script

print('Alimentando a tabela categorias...') 
categorias = open('./ETAPA_REL/insert_categorias.sql', 'r')
insert_db(categorias)

print('Alimentando a tabela funcionarios...')
funcionarios = open('./ETAPA_REL/insert_funcionarios.sql', 'r')
insert_db(funcionarios)

print('Alimentando a tabela vendas...')
vendas = open('./ETAPA_REL/insert_vendas.sql', 'r')
insert_db(vendas)

print('Fim da etapa insert_rel'.center(100, '-'))