from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        msg = request.form['message']
        conn = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DB']
        )
        cursor = conn.cursor()
        cursor.execute('INSERT INTO messages (content) VALUES (%s)', (msg,))
        conn.commit()
        cursor.close()
        conn.close()
        message = 'Message saved!'
    return render_template('index.html', message=message)
