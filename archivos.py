import os
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST'),
    user=os.getenv('MYSQL_USER'),
    password=os.getenv('MYSQL_PASSWORD'),
    database=os.getenv('MYSQL_DB')
)

db = connection.cursor()

# Función para obtener el ID del departamento insertado
def get_departamento_id(nombre):
    query = "SELECT id FROM Departamento WHERE nombre = %s"
    db.execute(query, (nombre,))
    result = db.fetchone()
    return result[0] if result else None

# Historia
carpetaHistoria = './Historia'
archivosHistoria = os.listdir(carpetaHistoria)

# Geografía
carpetaGeografia = './Geografia'
archivosGeografia = os.listdir(carpetaGeografia)

# Cultura
carpetaCultura = './Cultura'
archivosCultura = os.listdir(carpetaCultura)

# Imágenes
carpetaDirecccionImagenes = './direccion imagenes'
archivosDirecccionImagenes = os.listdir(carpetaDirecccionImagenes)

for archivo in archivosHistoria:
    departamento = archivo.split(sep='.')[0]
    
    # Insertar departamento
    query = "INSERT INTO Departamento (nombre) VALUES (%s)"
    db.execute(query, (departamento,))
    departamento_id = get_departamento_id(departamento)
    
    with open(carpetaHistoria + "/" + archivo, "r") as txt:
        parrafo1Historia = txt.readline().strip()
        parrafo2Historia = txt.readline().strip()
        
        # Insertar historia
        query2 = "INSERT INTO Historia (departamento_id, parrafo1, parrafo2) VALUES (%s, %s, %s)"
        db.execute(query2, (departamento_id, parrafo1Historia, parrafo2Historia,))

    with open(carpetaGeografia + "/" + archivo, "r") as txt:
        parrafo1Geografia = txt.readline().strip()
        parrafo2Geografia = txt.readline().strip()
        
        # Insertar geografía
        query3 = "INSERT INTO Geografia (departamento_id,parrafo1, parrafo2) VALUES (%s,%s, %s)"
        db.execute(query3, (departamento_id, parrafo1Geografia, parrafo2Geografia,))

    with open(carpetaCultura + "/" + archivo, "r") as txt:
        parrafo1Cultura = txt.readline().strip()
        parrafo2Cultura = txt.readline().strip()
        
        # Insertar cultura
        query4 = "INSERT INTO Cultura (departamento_id,parrafo1, parrafo2) VALUES (%s,%s, %s)"
        db.execute(query4, (departamento_id,parrafo1Cultura, parrafo2Cultura,))

    with open(carpetaDirecccionImagenes + "/" + archivo, "r") as txt:
        url_imagen1 = txt.readline().strip()
        url_imagen2 = txt.readline().strip()
        url_imagen3 = txt.readline().strip()
        url_imagen4 = txt.readline().strip()
        
        # Insertar imagen
        query2 = "INSERT INTO Imagen (departamento_id,url_imagen1, url_imagen2, url_imagen3, url_imagen4) VALUES (%s,%s, %s, %s, %s)"
        db.execute(query2, (departamento_id,url_imagen1, url_imagen2, url_imagen3, url_imagen4,))

# Commit de transacciones
connection.commit()

# Cerrar conexión
db.close()
connection.close()

print("Datos registrados exitosamente")
