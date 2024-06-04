from sqlalchemy.orm import sessionmaker

from database import Base, engine
from models import Cliente, Conta
from client_generator import create_random_cliente, create_random_conta

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

def create_cliente():
    """
    Create a new Cliente instance with random data and save it to the database.

    Returns:
        Cliente: The created Cliente instance.
    """
    novo_cliente = create_random_cliente()
    session.add(novo_cliente)
    session.commit()
    return novo_cliente

def create_conta(id_cliente):
    """
    Create a new Conta instance with random data for a given cliente and save it to the database.

    Args:
        id_cliente (int): The ID of the Cliente instance to associate with this Conta.

    Returns:
        Conta: The created Conta instance.
    """
    nova_conta = create_random_conta(id_cliente=id_cliente)
    session.add(nova_conta)
    session.commit()
    return nova_conta

# Generate and insert random Cliente and Conta data
for _ in range(10):
    cliente: Cliente = create_cliente()
    conta: Conta = create_conta(cliente.id)

# Retrieve all Cliente instances from the database
clientes = session.query(Cliente).all()

# Print all Cliente and associated Conta instances
for cliente in clientes:
    print(f'Cliente ID: {cliente.id}, Nome: {cliente.nome}, CPF: {cliente.cpf}, Endereco: {cliente.endereco}')
    for conta in cliente.contas:
        print(f'    Conta ID: {conta.id}, Tipo: {conta.tipo}, Agencia: {conta.agencia}, Num: {conta.num}, Saldo: {conta.saldo:.2f}')