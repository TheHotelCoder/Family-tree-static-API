"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, first_gen, second_gen, third_gen
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


@app.route('/first_gen', methods=['GET'])
def get_all_first_gen():    
    first_gen_all= first_gen.query.all()
    actual_first_gen = []
    for gen in first_gen_all:
        print(gen.serialize())
        actual_first_gen.append(gen.serialize())

    return jsonify(actual_first_gen), 200

@app.route('/second_gen', methods=['GET'])
def get_all_second_gen():    
    second_gen_all = second_gen.query.all()
    actual_second_gen = []
    for gen in second_gen_all:
        print(gen.serialize())
        actual_second_gen.append(gen.serialize())

    return jsonify(actual_second_gen), 200    

@app.route('/third_gen', methods=['GET'])
def get_all_third_gen():    
    third_gen_all = third_gen.query.all()
    actual_third_gen = []
    for gen in third_gen_all:
        print(gen.serialize())
        actual_third_gen.append(gen.serialize())

    return jsonify(actual_third_gen), 200    










# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
