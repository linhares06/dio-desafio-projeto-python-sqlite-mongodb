from decimal import Decimal
from faker import Faker

# Initialize Faker
fake = Faker()

# Function to generate a fake document
def create_random_cliente():
    return {
        "nome": fake.name(),
        "cpf": fake.unique.numerify(text='#########'),
        "endereco": fake.address(),
        "conta": [
            {
                "tipo": fake.random_element(elements=('Corrente', 'Poupança')),
                "agencia": fake.numerify(text='###'),
                "num": fake.random_int(min=10000, max=99999),
                "saldo":fake.pyfloat(left_digits=4, right_digits=2, positive=True)
            },
        ]
    }