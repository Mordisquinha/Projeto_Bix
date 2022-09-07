from database import Base
from sqlalchemy import Integer, Float, Column, DateTime, ForeignKey, String

class Vendas(Base):
    __tablename__ = 'vendas'
    id_venda = Column(Integer, primary_key=True)
    id_funcionario = Column(Integer, ForeignKey("funcionarios.id_funcionario"), nullable=False)
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=False)
    data_venda = Column(DateTime, nullable=False)
    venda = Column(Float, nullable=False)

class Funcionarios(Base):
    __tablename__ = 'funcionarios'
    id_funcionario = Column(Integer, primary_key=True)
    funcionario = Column(String(30), nullable=False)

class Categorias(Base):
    __tablename__ = 'categorias'
    id_categoria = Column(Integer, primary_key=True)
    categoria = Column(String(50), nullable=False)
