from faker import Faker

from models import Cliente, Conta

# Initialize Faker
fake = Faker()

# Generate random data using Faker
def create_random_cliente():
    nome = fake.name()
    cpf = fake.unique.numerify(text='#########')
    endereco = fake.street_address()
    return Cliente(nome=nome, cpf=cpf, endereco=endereco)

def create_random_conta(id_cliente):
    tipo = fake.random_element(elements=('Corrente', 'Poupança'))
    agencia = fake.numerify(text='###')
    num = fake.random_int(min=10000, max=99999)
    saldo = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    return Conta(tipo=tipo, agencia=agencia, num=num, saldo=saldo, id_cliente=id_cliente)