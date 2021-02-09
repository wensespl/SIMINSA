from flask import Flask, render_template, request, redirect, url_for, jsonify
import DB

nombre = ""
apellido = ""
tipe = ""

def load_user_data(usuario, contraseña):
    global nombre
    global apellido
    global tipe

    user = DB.usuarios.find_one({
        "ID": usuario,
        "Contraseña": contraseña
        })
    nombre = user["Nombres"]
    apellido = user["Apellidos"]
    tipe = user["Tipe"]

def get_paciente_data(dni):
    paciente = DB.pacientes.find_one({
        "DNI": dni
    })
    return paciente

def create_app():
    global nombre
    global apellido
    global tipe

    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            user = request.form['usuario']
            password = request.form['contraseña']
            if(DB.validate(user, password)):
                load_user_data(user, password)
                return redirect("home/")
        return render_template("index.html")

    @app.route("/home/")
    def home():
        if tipe == "UM":
            registrar = url_for('registrar')
            monitorear = url_for('home')
            prevenir = url_for('registrar')
        else:
            registrar = url_for('home')
            monitorear = url_for('registrar')
            prevenir = url_for('home')
        kwargs = {
            "nombre": nombre,
            "apellido": apellido,
            "registrar": registrar,
            "monitorear": monitorear,
            "prevenir": prevenir
        }
        return render_template("inicio.html", **kwargs)

    @app.route("/registrar/", methods=["GET", "POST"])
    def registrar():
        kwargs = {
            "nombre": nombre,
            "apellido": apellido
        }

        if request.method == "POST":
            dnibuscar = request.form['dnibuscar']
            if(dnibuscar):
                if(DB.buscarPaciente(dnibuscar)):
                    res = get_paciente_data(dnibuscar)
                    print(res["DNI"])
            #obtener datos del formulario
        return render_template("Registrar.html", **kwargs)

    return app
