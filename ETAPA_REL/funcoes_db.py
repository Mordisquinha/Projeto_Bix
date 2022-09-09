import pymysql.cursors 

class Connect_db:

    def conecta_db(self):
        try:
            self.conexao = pymysql.connect(host='mysqlpessoal.chfthweo9mu0.us-west-2.rds.amazonaws.com',
                                        user='gsantiago',
                                        password='11235813',
                                        database='rel',
                                        cursorclass=pymysql.cursors.DictCursor)
            return self.conexao
        except:
           return "conexão recusada."
