from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hola():
    try:
        conexion = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="testdb"
        )
        cursor = conexion.cursor()
        cursor.execute("SELECT 'Hola Mundo desde MySQL' ")
        resultado = cursor.fetchone()

        return f"✅ Conexión exitosa: {resultado[0]}"

    except Exception as e:
        return f"❌ Error de conexión: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)