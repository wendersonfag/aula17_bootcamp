from sqlalchemy import create_engine, select


# conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)


print("Conexão com SQLite estabelecida")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# with Session() as session:
#     novo_usuario = Usuario(nome='Flávia', idade=22)
#     session.add(novo_usuario)
#     session.commit()


with Session() as session:
    usuario = session.query(Usuario).filter_by(nome='Ana').first()
    print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")