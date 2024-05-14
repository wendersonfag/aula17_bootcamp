from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from desafio import Fornecedor, Produto



Base = declarative_base()

engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_preco')
).join(Produto, Fornecedor.id == Produto.fornecedor_id)\
.group_by(Fornecedor.nome).all()


for nome, total_preco in resultado:
    print(f"Fornecedor: {nome}, Total Preço: {total_preco}")



resultado2 = session.query(
    Produto.nome.label('produto'),
    func.count(Produto.preco).label('total')
)\
.group_by(Produto.nome).all()

for produto, qtd in resultado2:
    print(f"Produto: {produto}, Total: {qtd}")