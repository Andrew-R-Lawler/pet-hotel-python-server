import requests
from flask import Flask
import psycopg2

con = psycopg2.connect(
    host="Localhost",
    database="pet_hotel",
    user="andrewlawler",
    password="postgres",
    port=5432
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    cur = con.cursor()
    cur.close()
    return 'Hello'
