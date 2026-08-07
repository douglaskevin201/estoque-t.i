from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship



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
    hardware = relationship("ItemHardware", back_populates="item", uselist=False)



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

class ItemHardware(Base):
    __tablename__ = "hardware"

    item_id = Column(Integer, ForeignKey("itens.id"),primary_key=True)
    item = relationship("Item", back_populates="hardware")
    
    
    


Base.metadata.create_all(engine)