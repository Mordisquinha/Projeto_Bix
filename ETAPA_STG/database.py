import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(os.environ['ENGINE_SQLALCHEMY_PESSOAL_STG'],
    echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)