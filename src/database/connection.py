from pymongo import MongoClient
from src.config.settings import settings

client = None
database = None


def connect_to_mongo():
    global client, database

    client = MongoClient(
        settings.mongodb_uri,
        serverSelectionTimeoutMS=5000
    )

    client.admin.command("ping")

    database = client[settings.database_name]

    print("Conectado ao MongoDB com sucesso!")


def close_mongo_connection():
    global client, database

    if client:
        client.close()
        client = None
        database = None

    print("Conexão com MongoDB encerrada.")


def get_database():
    return database