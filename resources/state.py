from flask_restful import Resource
from models.state import StateModel

class State(Resource):
    def get(self, name):
        state = StateModel.find_by_state(name)
        if state:
             return state.json()
        return {'message': 'State not found'}, 404

    def post(self, name):
        if StateModel.find_by_state(name):
            return {"message": "A state with name '{}' already exists".format(name)}, 400

        state = StateModel(name)
        try:
            state.save_to_db()
            return {'message': 'State created'}, 200
        except:
            return {'message': 'An Error occured while creating the state'}, 500

    def delete(self, name):
        state = StateModel.find_by_state(name)
        if state:
            state.delete_from_db()
            return {"message": "State '{}' Deleted".format(name)}, 200
        return {"message": "State '{}' does not exist".format(name)}, 404


class States(Resource):
    def get(self):
        return {'states': [state.json() for state in StateModel.query.all()]}
