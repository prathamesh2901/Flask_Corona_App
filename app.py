#!/usr/bin/env python3


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.country import Country, Countries
from resources.state import State, States


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity) #/auth

api.add_resource(Countries, '/countries')
api.add_resource(Country, '/country/<string:name>')
api.add_resource(State, '/state/<string:country>/<string:name>')
api.add_resource(States, '/states')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
