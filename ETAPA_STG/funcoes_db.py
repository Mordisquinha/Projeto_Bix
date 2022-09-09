import psycopg2
from database import Session, engine

class Connect_db:
    def __init__(self):
        self.db = Session()
        self.select_venda = """SELECT * FROM public.venda"""
        self.engine = engine

    def conecta_db(self):
        print("conectando ao banco de dados...")
        try:
            self.conexao = psycopg2.connect(host='34.173.103.16', 
                                    database='postgres',
                                    user='junior', 
                                    password='|?7LXmg+FWL&,2(')
            print("conexão estabelecida.")

            return self.conexao
        except:
           return "conexão recusada."


    def consultar_db(self, sql):
        self.conexao = self.conecta_db()
        self.cursor = self.conexao.cursor()
        self.cursor.execute(sql)
        self.resultado = self.cursor.fetchall()
        self.registros = []
        for rec in self.resultado:
            self.registros.append(rec)
        self.conexao.close()
        return self.registros


    def truncate_vendas(self):
        self.db.execute('SET FOREIGN_KEY_CHECKS = 0;')
        self.db.execute('truncate vendas;')
        self.db.execute('SET FOREIGN_KEY_CHECKS = 1')

        return  'Tabela Limpa.'

    def truncate_categorias(self):
        self.db.execute('SET FOREIGN_KEY_CHECKS = 0;')
        self.db.execute('truncate categorias;')
        self.db.execute('SET FOREIGN_KEY_CHECKS = 1')

        return  'Tabela Limpa.'

    def truncate_funcionarios(self):
        self.db.execute('SET FOREIGN_KEY_CHECKS = 0;')
        self.db.execute('truncate funcionarios;')
        self.db.execute('SET FOREIGN_KEY_CHECKS = 1')

        return  'Tabela Limpa.'