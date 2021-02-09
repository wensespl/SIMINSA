import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.environ.get("MONGODB_URI"))
db = client.SIMINSADB
usuarios = db.Usuarios
pacientes = db.Pacientes
inmunizaciones = db.Inmunizaciones

def validate(user, contraseña):
    if(usuarios.find_one({"ID": user, "Contraseña": contraseña})):
        return True
    return False

def buscarPaciente(dni):
    if(pacientes.find_one({"DNI": dni})):
        return True
    return False