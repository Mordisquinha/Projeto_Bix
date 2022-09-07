from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('mysql://gsantiago:11235813@mysqlpessoal.chfthweo9mu0.us-west-2.rds.amazonaws.com/stg',
    echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)