import os
import pymysql.cursors 
from dotenv import load_dotenv

load_dotenv()
class Connect_db:

    def conecta_db(self):
        try:
            self.conexao = pymysql.connect(host=os.getenv("HOST"), 
                                           database=os.getenv("DATABASE"),
                                           user=os.getenv("USER"), 
                                           password=os.getenv("PASSWORD"),
                                           cursorclass=pymysql.cursors.DictCursor)
            return self.conexao
        except:
           return "conexão recusada."
