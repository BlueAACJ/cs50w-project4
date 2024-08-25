# 2022 Project-4
from flask import *
from funciones import *
from datetime import *
from config import *
from flask_session import *
from flask_mysqldb import MySQL

from funciones import limpiarlinea

#configuracion de flask 
try:
    app = Flask(__name__)
    app.config.from_object(FlaskConfig)
except Exception as ex:
    print("Error durante la configuracion de Flask {}".format(ex))

# Configuración de MySQL
try:
    mysql = MySQL(app)
    app.config.from_object(MySQLConfig)
except Exception as ex:
    print("Error durante la conexión: {}".format(ex))

# Index  
@app.route("/", methods=['GET', 'POST'])
def index():
    session.clear()
    db = mysql.connection.cursor()
    if request.method == "POST":
        username = request.form.get("username")
        session['username'] = request.form['username']

        if not username or username == '':
            flash('¡Tienes que introducir un usuario!')
            return redirect(url_for('index'))
        else:
            # verificamos si el usuario esta en la base de datos
            rows = db.execute("SELECT usuario FROM Puntuacion WHERE usuario = %s", (username,))

            # si es igual rows = 0 no esta registrado
            if rows == 0:
                # sql agregar usuario a la base de datos
                db.execute('INSERT INTO Puntuacion (usuario) VALUES(%s)', (username,))
                mysql.connection.commit()
                # Redireccionamos al home (pagina principal de sitio)
                return render_template("home.html")
            else:
                # renderizamos el home
                return render_template("home.html")
    db.close()
    # redireccionamos al index (Login)
    return render_template('index.html')

#home 
@app.route("/home", methods=['GET', 'POST'])
def home():
    # redireccionamos al home pagina principal del sitio 
    return render_template("home.html")

# Cultura 
@app.route("/cultura", methods=['GET', 'POST'])
def cultura():
    # redireccionamos al apartado de cultura 
    return render_template("cultura.html")

# geografia 
@app.route("/geografia", methods=['GET', 'POST'])
def geografia():
    # redireccionamos al  apartado de geografia 
    return render_template("geografia.html")

# historia 
@app.route("/historia", methods=['GET', 'POST'])
def historia():
    # redireccionamos al apartado de historia 
    return render_template("historia.html")

# explicacion_seccion 
@app.route("/explicacion_seccion", methods=['GET', 'POST'])
def cultuexplicacion_seccionra():
    # redireccionamos al apartado donde se le explica en que consiste la seccion de preguntados 
    return render_template("explicacion_seccion.html")

# Cerrar Sesion
@app.route("/cerrarsesion", methods=['GET', 'POST'])
def cerrarsesion():
    # Cerramos sesion 
    session.clear()
    # redireccionamos al index 
    return render_template("index.html")
    
# Pregunta
@app.route("/pregunta", methods=['GET', 'POST'])
def pregunta():
    # redireccionamos al apartado de pregunta 
    return render_template("pregunta.html")

# Ruta para ver el modelo de la pagina departameto recibe el nombre del departamento como argumento 
@app.route("/departamento_cultura/<string:nombre>", methods=['GET', 'POST'])
def departamento_cultura(nombre):
    db = mysql.connection.cursor()
    # traemos el id del departamento de la base de datos
    db.execute('SELECT id FROM departamento WHERE nombre = %s', (nombre,))
    id_departamento = db.fetchone()
    
    # traemos el texto de la base de datos
    query = "SELECT parrafo1,parrafo2 FROM Cultura WHERE departamento_id = %s"
    db.execute(query, (id_departamento,))
    texto = db.fetchone()

    # Separamos los textos  
    parrafo1 = texto[0]
    parrafo2 = texto[1]
    # Limpiamos el formato del texto con la funsion limpiarlinea
    parrafo1 = limpiarlinea(parrafo1)
    parrafo2 = limpiarlinea(parrafo2)

    query="SELECT url_imagen1,url_imagen2,url_imagen3,url_imagen4 FROM Imagen WHERE departamento_id = %s"
    db.execute(query, (id_departamento,))
    urls= db.fetchone()

    imagen1 = urls[0]
    imagen2 = urls[1]
    imagen3 = urls[2]
    imagen4 = urls[3]

    db.close()
    # renderizamos la pagina con el nombre del departamento, el parrafo1, el parrafo2, imagen1 e imagen2
    return render_template("departamento_cultura.html", dep=nombre, parrafo1=parrafo1, parrafo2=parrafo2, imagen1=imagen1, imagen2=imagen2, imagen3=imagen3, imagen4=imagen4)

# Ruta para ver el modelo de la pagina departameto recibe el nombre del departamento como argumento 
@app.route("/departamento_geografia/<string:nombre>", methods=['GET', 'POST'])
def departamento_geografia(nombre):
    db = mysql.connection.cursor()
    # traemos el id del departamento de la base de datos
    db.execute('SELECT id FROM departamento WHERE nombre = %s', (nombre,))
    id_departamento = db.fetchone()
    # traemos el texto de la base de datos
    query = "SELECT parrafo1,parrafo2 FROM Geografia WHERE departamento_id = %s"
    db.execute(query, (id_departamento,))
    texto = db.fetchone()

    # Separamos los textos  
    parrafo1 = texto[0]
    parrafo2 = texto[1]
    # Limpiamos el formato del texto con la funsion limpiarlinea
    parrafo1 = limpiarlinea(parrafo1)
    parrafo2 = limpiarlinea(parrafo2)

    query="SELECT url_imagen1,url_imagen2,url_imagen3,url_imagen4 FROM Imagen WHERE departamento_id = %s"
    db.execute(query, (id_departamento,))
    urls= db.fetchone()
    
    imagen1 = urls[0]
    imagen2 = urls[1]
    imagen3 = urls[2]
    imagen4 = urls[3]

    db.close()

    # renderizamos la pagina con el nombre del departamento, el parrafo1, el parrafo2, imagen1 e imagen2
    return render_template("departamento_geografia.html", dep=nombre, parrafo1=parrafo1, parrafo2=parrafo2, imagen1=imagen1, imagen2=imagen2, imagen3=imagen3, imagen4=imagen4)

# Ruta para ver el modelo de la pagina departameto recibe el nombre del departamento como argumento 
@app.route("/departamento_historia/<string:nombre>", methods=['GET', 'POST'])
def departamento_historia(nombre):
    db = mysql.connection.cursor()
    # traemos el id del departamento de la base de datos
    db.execute("SELECT id FROM departamento WHERE nombre = %s", (nombre,))
    id_departamento = db.fetchone()

    # traemos el texto de la base de datos
    query = "SELECT parrafo1,parrafo2 FROM Historia WHERE departamento_id = %s"
    db.execute(query, (id_departamento,))
    texto = db.fetchone()
    
    # Separamos los textos  
    parrafo1 = texto[0]
    parrafo2 = texto[1]
    # Limpiamos el formato del texto con la funsion limpiarlinea
    parrafo1 = limpiarlinea(parrafo1)
    parrafo2 = limpiarlinea(parrafo2)

    query="SELECT url_imagen1,url_imagen2,url_imagen3,url_imagen4 FROM Imagen WHERE departamento_id = %s"
    db.execute(query, (id_departamento,))
    urls= db.fetchone()
    
    imagen1 = urls[0]
    imagen2 = urls[1]
    imagen3 = urls[2]
    imagen4 = urls[3]

    db.close()

    # renderizamos la pagina con el nombre del departamento, el parrafo1, el parrafo2, imagen1 e imagen2
    return render_template("departamento_historia.html", dep=nombre, parrafo1=parrafo1, parrafo2=parrafo2, imagen1=imagen1, imagen2=imagen2, imagen3=imagen3, imagen4=imagen4)

# Ruta para la tabla de puntuaciones 
@app.route("/puntuaciones", methods=['GET','POST'])
def puntuaciones():
    # Conexion a la BD
    db = mysql.connection.cursor()
    # traemos las puntuaciones de la tabla de puntuaciones
    db.execute("SELECT usuario, puntuacion FROM Puntuacion")
    rows = db.fetchall()

    # Creacion del diccionario 
    columns = [column[0] for column in db.description]
    puntuaciones = [dict(zip(columns, row)) for row in rows]

    puntuaciones = [
    {**p, 'puntuacion': 'No hay registro'} if p['puntuacion'] is None else p 
    for p in puntuaciones
    ]

    puntuaciones = sorted(
    puntuaciones, 
    key=lambda x: int(x['puntuacion']) if x['puntuacion'] != 'No hay registro' else float('-inf'), 
    reverse=True
    )

    # Cerrar la conexion de la BD
    db.close()

    # redireccionamos a la tabla de puntuaciones con la informacion de las puntuaciones 
    return render_template("tablapuntuaciones.html", puntuaciones=puntuaciones)
