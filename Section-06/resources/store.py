from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        else:
            return {'message':f'No stores found with name "{name}"'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message':f"A store by the name of '{name}' already exists"}, 400
        
        new_store = StoreModel(name)
        try:
            new_store.save_to_db()
        except:
            return {'message': "An error occured while saving your store"}, 500
        return new_store.json(), 201
        
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message":f"Store ({name}) deleted from db."}
        else:
            return {"message":f"No store found with that name"}


class StoreList(Resource):
    TABLE_NAME = 'stores'
    
    def get(self):
        return{"stores": [store.json() for store in StoreModel.query.all()]}
        