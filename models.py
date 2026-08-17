from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from datetime import datetime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship



Base = declarative_base()
engine = create_engine('sqlite:///estoque.db')
Session = sessionmaker(bind=engine)
session = Session()

class Item(Base):

    """Item genérico do estoque de T.I.

    Representa qualquer equipamento cadastrado, independente da
    categoria. Categorias com atributos extras (Computador, Projetor)
    têm uma subclasse associada 1:1; categorias sem atributo extra
    (Hardware, Periférico, Acessório) usam apenas esta tabela, com
    uma subclasse vazia servindo só de âncora para filtro.
    """

    __tablename__ = 'itens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    categoria = Column(String(500), nullable=False)
    nome = Column(String(500), nullable=False)
    quantidade = Column(Integer, default=0)
    status = Column(String(1000))
    data = Column(DateTime, default=datetime.now)
    hardware = relationship("ItemHardware", back_populates="item", uselist=False, cascade="all, delete-orphan")
    periferico = relationship("ItemPeriferico", back_populates="item", uselist=False, cascade="all, delete-orphan")
    computador = relationship("ItemComputador", back_populates="item", uselist=False, cascade="all, delete-orphan")
    projetor = relationship("ItemProjetor", back_populates="item", uselist=False, cascade="all, delete-orphan")
    acessorio = relationship("ItemAcessorio", back_populates="item", uselist=False, cascade="all, delete-orphan")



    def aumentar_estoque(self, quantidade):

        """Aumenta a quantidade em estoque do item.
        Args:
            quantidade (int): valor a ser somado. Deve ser positivo.
        Raises:
            ValueError: se quantidade for menor ou igual a zero.
        """

        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        else:
            self.quantidade += quantidade


    def diminuir_estoque(self, quantidade):

        """Diminui a quantidade em estoque do item.
        
        Args:
            quantidade (int): valor a ser subtraido. Deve ser positivo
            e não pode ultrapassar a quantidade atual em estoque.
            
        Raises:
            ValueError: se quantidade for menor ou igual a zero, ou
            se a quantidade for maior que o valor atual em estoque."""

        if quantidade <= 0:
            raise ValueError("Numeros negativos não são permitidos.")
        elif quantidade > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        else:
            self.quantidade -= quantidade
           

class ItemHardware(Base):

    """Subclasse da categoria Hardware.

    Não possui atributos extras em relação a Item — existe apenas
    para permitir a associação via relationship e o filtro por
    categoria, sem duplicar dado que já está em Item.
    """

    __tablename__ = "hardware"

    item_id = Column(Integer, ForeignKey("itens.id"),primary_key=True)
    item = relationship("Item", back_populates="hardware")
    
 
class ItemPeriferico(Base):

    """Subclasse da categoria Periférico.

    Não possui atributos extras em relação a Item — existe apenas
    para permitir a associação via relationship e o filtro por
    categoria, sem duplicar dado que já está em Item.
    """

    __tablename__ = "periferico"

    item_id = Column(Integer, ForeignKey("itens.id"), primary_key=True)
    item = relationship("Item", back_populates="periferico")
    

class ItemComputador(Base):

    """Subclasse das categorias Desktop e Notebook.

    Guarda dados específicos de máquinas atribuídas a um setor ou
    responsável, que não fazem sentido nas demais categorias.

    Attributes:
        setor (str): setor da empresa onde o equipamento está alocado.
        responsavel (str): usuário responsável pelo equipamento.
        Recebe "T.I" quando não há responsável individual definido.
    """

    __tablename__ = "computador"

    item_id = Column(Integer, ForeignKey("itens.id"), primary_key=True)
    setor = Column(String(500))
    responsavel = Column(String(500))
    item = relationship("Item", back_populates="computador")

class ItemProjetor(Base):

    """Subclasse da categoria Projetor.

    Attributes:
        modelo (str): modelo do projetor.
    """
    
    __tablename__ = "projetor"

    item_id = Column(Integer, ForeignKey("itens.id"), primary_key=True)
    modelo = Column(String(500))
    item = relationship("Item", back_populates="projetor")

class ItemAcessorio(Base):

    """Subclasse da categoria Acessório.

    Não possui atributos extras em relação a Item — existe apenas
    para permitir a associação via relationship e o filtro por
    categoria, sem duplicar dado que já está em Item.
    """
    
    __tablename__ = "acessorio"

    item_id = Column(Integer, ForeignKey("itens.id"), primary_key=True)
    item = relationship("Item", back_populates="acessorio")


Base.metadata.create_all(engine)
