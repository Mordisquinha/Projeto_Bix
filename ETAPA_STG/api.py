import requests
import models
from funcoes_db import Connect_db

conexao = Connect_db()
db = conexao.db
truncando_tabela = conexao.truncate_funcionarios()

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

if __name__ == '__main__':
    print(truncando_tabela)
    if truncando_tabela:
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