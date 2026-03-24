from flask import Flask, render_template
import mysql.connector
import time

app = Flask(__name__)

def conectar_db():
    while True:
        try:
            conexion = mysql.connector.connect(
                host="db",
                user="root",
                password="root",
                database="testdb"
            )
            return conexion
        except:
            print("Esperando MySQL...")
            time.sleep(2)

@app.route('/')
def hola():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        # Crear tabla
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50)
            )
        """)

        # Insertar dato
        cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Roshell')")
        conexion.commit()

        # Consultar datos
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()

        return render_template("index.html", usuarios=usuarios)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)