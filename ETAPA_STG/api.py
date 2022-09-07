import requests
import models 
from database import Session


db = Session()

def truncando_tabela():
    db.execute('SET FOREIGN_KEY_CHECKS = 0;')
    db.execute('truncate funcionarios;')
    db.execute('SET FOREIGN_KEY_CHECKS = 1')

    return  'Tabela Limpa.'

def insere_funcionario(id, nome_funcionario):
    novo_funcionario = models.Funcionarios(
        id_funcionario = id,
        funcionario = nome_funcionario
    )

    db.add(novo_funcionario)
    db.commit()
    return funcionario.text

id_max = 1
loop = True

limpar_tabela = truncando_tabela()
print(limpar_tabela)
if limpar_tabela:
    while loop:
        link = f'https://us-central1-bix-tecnologia-prd.cloudfunctions.net/api_challenge_junior?id={id_max}'
        funcionario = requests.get(link)

        if funcionario.text == 'The argument is not correct':
            loop = False
        else:
            add = insere_funcionario(id=id_max, nome_funcionario=funcionario.text)
            print(f'Adicionando {id_max} - {add} ao banco de dados bancoAPI na tabela de funcionarios.')
            id_max += 1
else:
    print('Não foi possível limpar a tabela.')
print('Fim da etapa API'.center(100, '-'))