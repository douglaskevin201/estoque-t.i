from sqlalchemy import Column, Integer, String, DateTime, create_engine
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker
from time import sleep


Base = declarative_base()
engine = create_engine('sqlite:///estoque.db')
Session = sessionmaker(bind=engine)
session = Session()

class Item(Base):
    __tablename__ = 'itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(500), nullable=False)
    nome = Column(String(500), nullable=False)
    quantidade = Column(Integer, default=0)
    data = Column(DateTime, default=datetime.now)




    def aumentar_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        else:
            self.quantidade += quantidade


    def diminuir_estoque(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Numeros negativos não são permitidos.")
        elif quantidade > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        else:
            self.quantidade -= quantidade


        

            

    def exibir_dados(self):
        return f"ID: {self.id} | Categoria: {self.categoria} | Nome: {self.nome} | Quantidade: {self.quantidade} | Cadastrado: {self.data}"


Base.metadata.create_all(engine)