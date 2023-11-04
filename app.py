from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://scrappy_db_user:oFBmcMPwf5TmH6EowkCoVDGqJt7PljDH@dpg-cl3b9pquuipc738ana7g-a/scrappy_db")
    conn.close()
    return "Database Connection Successful"