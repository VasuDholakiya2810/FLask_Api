from flask_restful import Resource
from models.stores import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store Not Found...".format(name)}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store {name} is already exists".format(name=name)}, 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete()
            return {"message": "item deleted..."}
        return {"message": "No {} store".format(name)}


class StoreList(Resource):
    def get(self):
        return {"Stores": [item.json() for item in StoreModel.query.all()]}
