from flask_restful import Resource, reqparse
from mycode.Models.ItemModel import ItemModel

class ItemResource(Resource):
    def get(self, itemId):
        myobject = ItemModel(itemId, None, None)
        mydata = myobject.finditembyid()
        if mydata:
            return {"result": mydata.returnJSON()}, 200
        return {"message": "Item not found"}, 404

    def put(self, itemId):
        myparser = reqparse.RequestParser()
        myparser.add_argument('name', type=str, required=True, help='Name is required')
        myparser.add_argument('price', type=float, required=True, help='Price is required')
        datapassed = myparser.parse_args()

        itemtoupdate = ItemModel(itemId, datapassed['name'], datapassed['price'])
        returnvalue = itemtoupdate.updateItem()
        if returnvalue == 0:
            return datapassed, 200
        elif returnvalue == -1:
            return {"message": "Item Not Found"}, 404
        else:
            return {"message": "Internal Server Error"}, 500

    def delete(self, itemId):
        myobject = ItemModel(itemId, None, None)
        mydata = myobject.deleteItem()
        if mydata == 0:
            return {"message": "Item deleted successfully"}, 200
        elif mydata == -1:
            return {"message": "Item not found"}, 404
        else:
            return {"message": "Internal server error"}, 500

class PostItemResource(Resource):
    def post(self):
        myparser = reqparse.RequestParser()
        myparser.add_argument('name', type=str, required=True, help='Name is required')
        myparser.add_argument('price', type=float, required=True, help='Price is required')
        datapassed = myparser.parse_args()

        myobject = ItemModel(None, datapassed['name'], datapassed['price'])
        mydata = myobject.insertItem()
        if mydata == 0:
            return datapassed, 201
        elif mydata == -1:
            return {"message": "Item already exist"}, 400
        else:
            return {"message": "Internal server error"}, 500
