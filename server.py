import requests
from flask import Flask, jsonify, json, request
from flask_cors import CORS
import psycopg2

con = psycopg2.connect(
    host="Localhost",
    database="pet_hotel",
    user="postgres",
    password="postgres",
    port=5432
)

app = Flask(__name__)
CORS(app)


@app.route('/owner', methods=['GET'])
def hello_world():
    cur = con.cursor()
    cur.execute("select * from owners")
    rows = cur.fetchall()
    return jsonify(rows)


@app.route('/owner', methods=['POST'])
def post():
    cur = con.cursor()
    owner = request.get_json()
    first_name = owner["firstName"]
    last_name = owner["lastName"]
    cur.execute("insert into owners (first_name, last_name) values (%s, %s);",
                (first_name, last_name))
    con.commit()
    cur.close()
    return 'Hello'


@app.route('/owner', methods=['DELETE'])
def delete():
    cur = con.cursor()
    owner = request.get_json()
    owner_id = owner["key"]
    print(owner_id)
    cur.execute("delete from pets where owners_id=%s;", (owner_id,))
    cur.execute("delete from owners where id=%s;", (owner_id,))
    con.commit()
    cur.close()
    return 'Aloha'


@app.route('/pet', methods=["GET"])
def get_pets():
    cur = con.cursor()
    cur.execute("select * from pets")
    rows = cur.fetchall()
    return jsonify(rows)


@app.route('/pet', methods=["POST"])
def post_pet():
    cur = con.cursor()
    pet = request.get_json()
    pet_name = pet["name"]
    pet_color = pet["color"]
    pet_breed = pet["breed"]
    owner_id = pet["owner"]
    cur.execute("insert into pets (name, breed, color, owners_id) values (%s, %s, %s, %s);",
                (pet_name, pet_breed, pet_color, owner_id))
    print(pet_name, pet_color, pet_breed, owner_id)
    con.commit()
    cur.close()
    return 'I like candy'


@app.route('/pet', methods=["PUT"])
def update_pet():
    cur = con.cursor()
    print(request.get_json)
    pet = request.get_json()
    print(pet)
    pet_id = pet["key"]

    cur.execute(
        "update pets set is_checked_in = NOT is_checked_in where id=%s;", (pet_id,))

    return 'hello'
