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

def guardarDatosPa(datos):
    sintomas = {
        "s1": "",
        "s2": "",
        "s3": "",
        "s4": "",
        "s5": "",
        "s6": "",
        "s7": ""
    }
    if datos.get("s1"):
        sintomas['s1'] = "on"
    if datos.get("s2"):
        sintomas['s2'] = "on"
    if datos.get("s3"):
        sintomas['s3'] = "on"
    if datos.get("s4"):
        sintomas['s4'] = "on"
    if datos.get("s5"):
        sintomas['s5'] = "on"
    if datos.get("s6"):
        sintomas['s6'] = "on"
    if datos.get("s7"):
        sintomas['s7'] = "on"
    pacientes.insert_one({
        "DNI": datos['dni'],
        "Nombre1": datos['nombre1'],
        "Nombre2": datos['nombre2'],
        "Apellido1": datos['apellido1'],
        "Apellido2": datos['apellido2'],
        "FN": datos['fecha_nacimiento'],
        "Genero": datos['genero'],
        "Telf": datos['telefono'],
        "Dep": datos['departamento'],
        "Dist": datos['distrito'],
        "Calle": datos['calle'],
        "Sintomas": sintomas,
        "Otros": datos['otros'],
        "EstPa": datos['estadop']
    })
    inmunizaciones.insert_one({
        "DNI": datos['dni'],
        "FV1": datos['fecha_vacuna1'],
        "EV1": datos['estado_vacuna1'],
        "Lab": datos['lab1'],
        "FV2": datos['fecha_vacuna2'],
        "EV2": datos['estado_vacuna2'],
    })