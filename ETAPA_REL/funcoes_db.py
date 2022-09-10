import os
import pymysql.cursors 

class Connect_db:
    def __init__(self):
        self.host = os.environ['HOST_PESSOAL']
        self.database = os.environ['DATABASE_PESSOAL']
        self.user = os.environ['USER_PESSOAL']
        self.password = os.environ['PASSWORD_PESSOAL']


    def conecta_db(self):
        try:
            self.conexao = pymysql.connect(host=self.host,
                                        user= self.user,
                                        password=self.password,
                                        database=self.database,
                                        cursorclass=pymysql.cursors.DictCursor)
            return self.conexao
        except:
           return "conexÃ£o recusada."
