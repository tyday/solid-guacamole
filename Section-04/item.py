import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

def queryDB(query,qry_variables=None):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    if qry_variables:
        result = cursor.execute(query, qry_variables)
    else:
        result = cursor.execute(query)
    rows = result.fetchall()
    connection.commit()
    connection.close()
    return rows



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'price', type=float,required=True,help='Price is required'
    )

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return {'item': {'name':row[0], 'price':row[1]}}
        else:
            return {'message': 'Item not found'}, 404

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item': {'name':row[0], 'price':row[1]}}
        

    def post(self, name):
        if self.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400
        
        data = Item.parser.parse_args()
        
        item = {'name':name, 'price':data['price']}

        query = "INSERT INTO items VALUES (?,?)"
        queryDB(query,(item['name'], item['price']))

        return item, 201
    
    def delete(self, name):
        
        # global items
        # items = list(filter(lambda x: x['name'] != name, items))
        if Item.find_by_name(name):
            query = "DELETE FROM items WHERE name=?"
            queryDB(query,(name,))
            return {'message': 'Item deleted'}
        return {'message':'Item not found.'}, 404

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name']== name, items), None)
        if item is None:
            item = {'name': name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        print(item,data)
            
        return {'item':item}

class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        rows = result.fetchall()
        connection.close()
        items = []
        for row in rows:
            items.append({'name':row[0],'price':row[1]})
        if items:
            return {'items': items}
        return {'message':'No items found'}