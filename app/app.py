from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

# Database Configuration from Environment Variables
db_config = {
    "host": os.getenv("DB_HOST", "mysql"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "root"),
    "database": os.getenv("DB_NAME", "messages_db"),
}

def get_db_connection():
    """Establish a connection to the MySQL database"""
    conn = mysql.connector.connect(**db_config)
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == "POST":
        message = request.form["message"]
        cursor.execute("INSERT INTO messages (text) VALUES (%s)", (message,))
        conn.commit()
    
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    
    conn.close()
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

