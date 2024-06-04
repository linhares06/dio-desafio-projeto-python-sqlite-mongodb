from database import Database
from client_generator import create_random_cliente

def main():
    """
    Main function to insert and retrieve client documents in/from the MongoDB collection.
    
    Steps:
    1. Initialize the Database connection.
    2. Insert a predefined client document.
    3. Generate and insert multiple random client documents.
    4. Retrieve and print all client documents.
    5. Retrieve and print a specific client document by name.
    """
    # Initialize the Database connection
    db = Database()

    # Predefined client document
    client: dict = {
        "nome": "Maria",
        "cpf": "123456788",
        "endereco": "Avenida Presidente Vargas 123",
        "conta": [
            {
                "tipo": "Corrente",
                "agencia": "123",
                "num": 10001,
                "saldo": 2020.25,
            },
        ]
    }

    # Insert the predefined client document into the collection
    db.clientes_collection.insert_one(client)

    # List to store multiple random client documents
    clients: list[dict] = []

    # Generate and append 5 random client documents to the list
    for _ in range(5):
        clients.append(create_random_cliente())

    # Insert multiple random client documents into the collection
    db.clientes_collection.insert_many(clients)

    # Retrieve all client documents from the collection
    all_clients = list(db.clientes_collection.find())

    # Retrieve a specific client document by name from the collection
    one_client = db.clientes_collection.find_one({"nome": "Maria"})

    # Print the specific client document
    print(one_client)

    # Print all client documents
    for client in all_clients:
        print(client)

if __name__ == "__main__":
    main()