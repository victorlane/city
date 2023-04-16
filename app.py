from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Example data store
items = []


# Resource class
class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x["name"] == name, items), None)
        return {"item": item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x["name"] == name, items), None):
            return {"message": f"Item with name {name} already exists."}, 400

        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {"items": items}


# Adding resources to the API
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

if __name__ == "__main__":
    app.run(debug=True)
