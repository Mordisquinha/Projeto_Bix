from database import Base, engine
from models import Vendas, Funcionarios, Categorias

Base.metadata.create_all(engine)
print("database criado")