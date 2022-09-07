from email.policy import default
from database import Base
from sqlalchemy import Integer, Float, Column, DateTime, ForeignKey, String

class Vendas(Base):
    __tablename__ = 'vendas'
    id_venda = Column(Integer, primary_key=True)
    id_funcionario = Column(Integer, ForeignKey("funcionarios.id_funcionario"))
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"))
    data_venda = Column(DateTime)
    venda = Column(Float)
    insercao_base = Column(DateTime, default='Null')
    exclusao_logica = Column(DateTime, default='Null')

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id_funcionario = Column(Integer, primary_key=True)
    funcionario = Column(String(30))
    insercao_base = Column(DateTime, default='Null')
    exclusao_logica = Column(DateTime, default='Null')

class Categorias(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True)
    categoria = Column(String(50))
    insercao_base = Column(DateTime, default='Null')
    exclusao_logica = Column(DateTime, default='Null')
