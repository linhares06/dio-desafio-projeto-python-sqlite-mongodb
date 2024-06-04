from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from database import Base

class Cliente(Base):
    __tablename__ = 'cliente'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(9), nullable=False, unique=True)
    endereco = Column(String, nullable=False)

    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'conta'
    
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    num = Column(Integer, nullable=False)
    saldo = Column(Numeric, nullable=False)
    id_cliente = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    
    cliente = relationship('Cliente', back_populates='contas')