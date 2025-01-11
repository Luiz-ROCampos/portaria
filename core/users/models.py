from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

#******************** Criando o banco de dados ******************** 
engine = create_engine('sqlite:///db_portaria.db', echo=True)

#******************** Criando a sessão ******************** 
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, unique=True, nullable=False)
    senha = Column("senha", String, nullable=False)
    tipo = Column("tipo", String, nullable=False)

    def __init__(self, nome, senha, tipo):
        self.nome = nome
        self.senha = senha
        self.tipo = tipo

#******************** Verificar usuário ******************** 
def check_user(usuario, senha):
        
        user = session.query(User).filter_by(nome=usuario).first()
        if user.senha == senha:
            return True
        else:
            return False
        

Base.metadata.create_all(engine)

# Usuarios do db
#user = User(nome="Lider", senha='liderport', tipo="liderança")
#user = User(nome="admin", senha='admin', tipo="portaria")
#session.add(user)
#session.commit()


