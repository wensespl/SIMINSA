import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

# User Config
nombre = ""
apellido = ""

def create_app():

    load_dotenv()

    app = Flask(__name__)
    # Mongo Config
    client = MongoClient(os.environ.get("MONGODB_URI"))
    db = client.test
    users = db.users

    @app.route("/", methods=["GET", "POST"])
    def index():
        global nombre
        global apellido
        if request.method == "POST":
            user = request.form.get("usuario")
            dni = request.form.get("dni_number")
            if(users.find_one({"nombre": user, "DNI": dni})):
                res = users.find_one({"nombre": user, "DNI": dni})
                nombre = res["nombre"]
                apellido = res["apellido"]
                return redirect("home/")
        return render_template("login.html")

    @app.route("/home/")
    def home():
        global nombre
        global apellido
        return render_template("inicio.html", nombre=nombre, apellido=apellido)

    return app
