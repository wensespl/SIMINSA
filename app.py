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

def clear_user_data():
    global nombre
    global apellido
    global tipe

    nombre = ""
    apellido = ""
    tipe = ""

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

    @app.route("/logout/")
    def logout():
        clear_user_data()
        return redirect(url_for('index'))

    @app.route("/home/")
    def home():
        if(nombre == ""):
            return redirect(url_for('index'))
        if tipe == "UM":
            registrar = url_for('registrar')
            monitorear = url_for('home')
            prevenir = url_for('prevenir')
        else:
            registrar = url_for('home')
            monitorear = url_for('monitorear')
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
        if(nombre == ""):
            return redirect(url_for('index'))
        dni_buscar = ""
        dni_p = ""
        nombre1_p = ""
        nombre2_p = ""
        apellido1_p = ""
        apellido2_p = ""
        est1_p = ""
        est2_p = ""
        M = ""
        F = ""
        telf_p = ""
        fechana_p = ""
        D1 = ""
        D2 = ""
        D3 = ""
        D4 = ""
        D5 = ""
        D6 = ""
        D7 = ""
        D8 = ""
        D9 = ""
        D10 = ""
        D11 = ""
        D12 = ""
        D13 = ""
        D14 = ""
        D15 = ""
        D16 = ""
        D17 = ""
        D18 = ""
        D19 = ""
        D20 = ""
        D21 = ""
        D22 = ""
        D23 = ""
        D24 = ""
        D25 = ""
        dist_name_p = ""
        calle_name_p = ""
        s1_p = ""
        s2_p = ""
        s3_p = ""
        s4_p = ""
        s5_p = ""
        s6_p = ""
        s7_p = ""
        otros_p = ""
        estado1_v = ""
        estado2_v = ""
        estado3_v = ""
        fv1 = ""
        lab1 = ""
        lab2 = ""
        estado4_v = ""
        estado5_v = ""
        estado6_v = ""
        fv2 = ""
        if tipe == "UM":
            registrar = url_for('registrar')
            monitorear = url_for('home')
            prevenir = url_for('prevenir')
        else:
            registrar = url_for('home')
            monitorear = url_for('monitorear')
            prevenir = url_for('home')
        if request.method == "POST":
            if(request.form['boton'] == 'Buscar'):
                dnibuscar = request.form['dnibuscar']
                if(DB.buscarPaciente(dnibuscar)):
                    paciente = DB.pacientes.find_one({
                        "DNI": dnibuscar
                        })
                    inmunizaciones = DB.inmunizaciones.find_one({
                        "DNI": dnibuscar
                    })
                    dni_p = paciente['DNI']
                    nombre1_p = paciente['Nombre1']
                    nombre2_p = paciente['Nombre2']
                    apellido1_p = paciente['Apellido1']
                    apellido2_p = paciente['Apellido2']
                    if(paciente['EstPa'] == "Estable"):
                        est1_p = "selected"
                    else:
                        est2_p = "selected"
                    if(paciente['Genero'] == "Masculino"):
                        M = "selected"
                    else:
                        F = "selected"
                    telf_p = paciente['Telf']
                    fechana_p = paciente['FN']
                    if(paciente['Dep'] == "Amazonas"):
                        D1 = "selected"
                    elif(paciente['Dep'] == "Ancash"):
                        D2 = "selected"
                    elif(paciente['Dep'] == "Apurímac"):
                        D3 = "selected"
                    elif(paciente['Dep'] == "Arequipa"):
                        D4 = "selected"
                    elif(paciente['Dep'] == "Ayacucho"):
                        D5 = "selected"
                    elif(paciente['Dep'] == "Cajamarca"):
                        D6 = "selected"
                    elif(paciente['Dep'] == "Callao"):
                        D7 = "selected"
                    elif(paciente['Dep'] == "Cusco"):
                        D8 = "selected"
                    elif(paciente['Dep'] == "Huancavelica"):
                        D9 = "selected"
                    elif(paciente['Dep'] == "Huánuco"):
                        D10 = "selected"
                    elif(paciente['Dep'] == "Ica"):
                        D11 = "selected"
                    elif(paciente['Dep'] == "Junín"):
                        D12 = "selected"
                    elif(paciente['Dep'] == "La Libertad"):
                        D13 = "selected"
                    elif(paciente['Dep'] == "Lambayeque"):
                        D14 = "selected"
                    elif(paciente['Dep'] == "Lima"):
                        D15 = "selected"
                    elif(paciente['Dep'] == "Loreto"):
                        D16 = "selected"
                    elif(paciente['Dep'] == "Madre de Dios"):
                        D17 = "selected"
                    elif(paciente['Dep'] == "Moquegua"):
                        D18 = "selected"
                    elif(paciente['Dep'] == "Pasco"):
                        D19 = "selected"
                    elif(paciente['Dep'] == "Piura"):
                        D20 = "selected"
                    elif(paciente['Dep'] == "Puno"):
                        D21 = "selected"
                    elif(paciente['Dep'] == "San martin"):
                        D22 = "selected"
                    elif(paciente['Dep'] == "Tacna"):
                        D23 = "selected"
                    elif(paciente['Dep'] == "Tumbes"):
                        D24 = "selected"
                    else:
                        D25 = "selected"
                    dist_name_p = paciente['Dist']
                    calle_name_p = paciente['Calle']
                    if(paciente['Sintomas']['s1'] == "on"):
                        s1_p = "checked"
                    if(paciente['Sintomas']['s2'] == "on"):
                        s2_p = "checked"
                    if(paciente['Sintomas']['s3'] == "on"):
                        s3_p = "checked"
                    if(paciente['Sintomas']['s4'] == "on"):
                        s4_p = "checked"
                    if(paciente['Sintomas']['s5'] == "on"):
                        s5_p = "checked"
                    if(paciente['Sintomas']['s6'] == "on"):
                        s6_p = "checked"
                    if(paciente['Sintomas']['s7'] == "on"):
                        s7_p = "checked"
                    otros_p = paciente['Otros']
                    if(inmunizaciones['EV1'] == "Recibida"):
                        estado1_v = "selected"
                    elif(inmunizaciones['EV1'] == "No recibida"):
                        estado2_v = "selected"
                    else:
                        estado3_v = "selected"
                    fv1 = inmunizaciones['FV1']
                    if(inmunizaciones['Lab'] == "Sinopharm"):
                        lab1 = "selected"
                    else:
                        lab2 = "selected"
                    if(inmunizaciones['EV2'] == "Recibida"):
                        estado4_v = "selected"
                    elif(inmunizaciones['EV2'] == "No recibida"):
                        estado5_v = "selected"
                    else:
                        estado6_v = "selected"
                    fv2 = inmunizaciones['FV2']
            else:
                if(not DB.buscarPaciente(request.form['dni'])):
                    DB.guardarDatosPa(request.form)
                return redirect(url_for('registrar'))
        kwargs = {
            "nombre": nombre,
            "apellido": apellido,
            "dni_buscar": dni_buscar,
            "dni_p": dni_p,
            "nombre1_p": nombre1_p,
            "nombre2_p": nombre2_p,
            "apellido1_p": apellido1_p,
            "apellido2_p": apellido2_p,
            "est1_p": est1_p,
            "est2_p": est2_p,
            "M": M,
            "F": F,
            "telf_p": telf_p,
            "fechana_p": fechana_p,
            "D1": D1,
            "D2": D2,
            "D3": D3,
            "D4": D4,
            "D5": D5,
            "D6": D6,
            "D7": D7,
            "D8": D8,
            "D9": D9,
            "D10": D10,
            "D11": D11,
            "D12": D12,
            "D13": D13,
            "D14": D14,
            "D15": D15,
            "D16": D16,
            "D17": D17,
            "D18": D18,
            "D19": D19,
            "D20": D20,
            "D21": D21,
            "D22": D22,
            "D23": D23,
            "D24": D24,
            "D25": D25,
            "dist_name_p": dist_name_p,
            "calle_name_p": calle_name_p,
            "s1_p": s1_p,
            "s2_p": s2_p,
            "s3_p": s3_p,
            "s4_p": s4_p,
            "s5_p": s5_p,
            "s6_p": s6_p,
            "s7_p": s7_p,
            "otros_p": otros_p,
            "estado1_v": estado1_v,
            "estado2_v": estado2_v,
            "estado3_v": estado3_v,
            "fv1": fv1,
            "lab1": lab1,
            "lab2": lab2,
            "estado4_v": estado4_v,
            "estado5_v": estado5_v,
            "estado6_v": estado6_v,
            "fv2": fv2,
            "registrar": registrar,
            "monitorear": monitorear,
            "prevenir": prevenir
        }
        return render_template("Registrar.html", **kwargs)

    @app.route("/prevenir/", methods=["GET", "POST"])
    def prevenir():
        if(nombre == ""):
            return redirect(url_for('index'))
        if tipe == "UM":
            registrar = url_for('registrar')
            monitorear = url_for('home')
            prevenir = url_for('prevenir')
        else:
            registrar = url_for('home')
            monitorear = url_for('monitorear')
            prevenir = url_for('home')

        pag = DB.pacientes.find({})
        for x in pag:
            if(x['EstPa'] == "Grave"):
                print(x)
        kwargs = {
            "nombre": nombre,
            "apellido": apellido,
            "registrar": registrar,
            "monitorear": monitorear,
            "prevenir": prevenir
        }
        return render_template("Prevenir.html", **kwargs)

    @app.route("/monitorear/", methods=["GET", "POST"])
    def monitorear():
        if(nombre == ""):
            return redirect(url_for('index'))
        if tipe == "UM":
            registrar = url_for('registrar')
            monitorear = url_for('home')
            prevenir = url_for('prevenir')
        else:
            registrar = url_for('home')
            monitorear = url_for('monitorear')
            prevenir = url_for('home')
        dni_buscar = ""
        estado_buscar = ""
        nombresapellidos_p = ""
        direccion_p = ""
        M = ""
        F = ""
        telf_p = ""
        fechana_p = ""
        estado_p = ""
        s1_p = ""
        s2_p = ""
        s3_p = ""
        s4_p = ""
        s5_p = ""
        s6_p = ""
        s7_p = ""
        otros_p = ""
        estado1_v = ""
        estado2_v = ""
        estado3_v = ""
        fv1 = ""
        estado4_v = ""
        estado5_v = ""
        estado6_v = ""
        fv2 = ""
        if request.method == "POST":
            if(request.form['boton'] == 'Buscar'):
                dni_buscar = request.form['dnibuscar']
                est_buscar = request.form['estadobuscar']
                if(DB.buscarPacienteEstado(dni_buscar, est_buscar)):
                    paciente = DB.pacientes.find_one({
                        "DNI": dni_buscar
                        })
                    inmunizaciones = DB.inmunizaciones.find_one({
                        "DNI": dni_buscar
                        })
                    nombresapellidos_p = paciente['Nombre1']+" "+paciente['Nombre2']+" "+paciente['Apellido1']+" "+paciente['Apellido2']
                    direccion_p = paciente['Dep']+","+paciente['Dist']+","+paciente['Calle']
                    if(paciente['Genero'] == "Masculino"):
                        M = "selected"
                    else:
                        F = "selected"
                    telf_p = paciente['Telf']
                    fechana_p = paciente['FN']
                    estado_p = paciente['EstPa']
                    if(paciente['Sintomas']['s1'] == "on"):
                        s1_p = "checked"
                    if(paciente['Sintomas']['s2'] == "on"):
                        s2_p = "checked"
                    if(paciente['Sintomas']['s3'] == "on"):
                        s3_p = "checked"
                    if(paciente['Sintomas']['s4'] == "on"):
                        s4_p = "checked"
                    if(paciente['Sintomas']['s5'] == "on"):
                        s5_p = "checked"
                    if(paciente['Sintomas']['s6'] == "on"):
                        s6_p = "checked"
                    if(paciente['Sintomas']['s7'] == "on"):
                        s7_p = "checked"
                    otros_p = paciente['Otros']
                    if(inmunizaciones['EV1'] == "Recibida"):
                        estado1_v = "selected"
                    elif(inmunizaciones['EV1'] == "No recibida"):
                        estado2_v = "selected"
                    else:
                        estado3_v = "selected"
                    fv1 = inmunizaciones['FV1']
                    if(inmunizaciones['EV2'] == "Recibida"):
                        estado4_v = "selected"
                    elif(inmunizaciones['EV2'] == "No recibida"):
                        estado5_v = "selected"
                    else:
                        estado6_v = "selected"
                    fv2 = inmunizaciones['FV2']
            else:
                DB.guardarDatosMo(request.form)
                return redirect(url_for('monitorear'))
        '''
        pag = DB.pacientes.find({
                "EstPa": "Grave"
                })
        print(pag)
        '''
        kwargs = {
            "nombre": nombre,
            "apellido": apellido,
            "registrar": registrar,
            "monitorear": monitorear,
            "prevenir": prevenir,
            "nombresapellidos_p": nombresapellidos_p,
            "direccion_p": direccion_p,
            "M": M,
            "F": F,
            "telf_p": telf_p,
            "fechana_p": fechana_p,
            "estado_p": estado_p,
            "s1_p": s1_p,
            "s2_p": s2_p,
            "s3_p": s3_p,
            "s4_p": s4_p,
            "s5_p": s5_p,
            "s6_p": s6_p,
            "s7_p": s7_p,
            "otros_p": otros_p,
            "estado1_v": estado1_v,
            "estado2_v": estado2_v,
            "estado3_v": estado3_v,
            "fv1": fv1,
            "estado4_v": estado4_v,
            "estado5_v": estado5_v,
            "estado6_v": estado6_v,
            "fv2": fv2,
        }
        return render_template("Monitorear.html", **kwargs)

    return app
