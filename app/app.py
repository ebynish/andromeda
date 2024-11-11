import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Database connection settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "andromeda_db")
DB_USER = os.getenv("POSTGRES_USER", "andromeda_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "andromeda_password")

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

@app.route("/")
def home():
    conn = get_db_connection()
    if conn is None:
        return jsonify(message="Failed to connect to the database"), 500

    cur = conn.cursor()
    cur.execute("SELECT 'Hello from PostgreSQL!'")
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    
    return jsonify(message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
