from funcoes_db import Connect_db


def insert_db(sql):
    with sql as arquivo_sql:
        script = arquivo_sql.read().replace('\n', ' ')

    conexao = Connect_db()
    conexao = conexao.conecta_db()

    with conexao:
        with conexao.cursor() as cursor:
            cursor.execute(script)
        conexao.commit()
    return script

print('Alimentando a tabela categorias...') 
categorias = open('./insert_categorias.sql', 'r')
insert_db(categorias)

print('Alimentando a tabela funcionarios...')
funcionarios = open('./insert_funcionarios.sql', 'r')
insert_db(funcionarios)

print('Alimentando a tabela vendas...')
vendas = open('./insert_vendas.sql', 'r')
insert_db(vendas)

print('Fim da etapa insert_rel'.center(100, '-'))
