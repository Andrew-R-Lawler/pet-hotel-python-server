import requests
from flask import Flask, jsonify, json
import psycopg2

con = psycopg2.connect(
    host="Localhost",
    database="pet_hotel",
    user="andrewlawler",
    password="postgres",
    port=5432
)

app = Flask(__name__)

@app.route('/owner', methods=['GET'])
def hello_world():
    cur = con.cursor()
    cur.execute("select * from owners")
    rows = cur.fetchall()
    return jsonify(rows)
