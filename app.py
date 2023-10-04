from flask import Flask, request, jsonify
from db import SmartphoneDB
db=SmartphoneDB("db.json")

app = Flask(__name__)
db = SmartphoneDB('db.json')

@app.route('/')
def start():
    return 'Hello'


## view all smartphone
@app.route('/smartphones', methods=['GET'])
def get_all_smartphones():
    """Returns all smartphones in the database"""
    return jsonify(db.brands())


# view all brands
@app.route('/smartphones/brands', methods=['GET'])
def get_all_brands():
    """Returns all brands in the database"""
    text=["Apple","Redmi","Nokia","Huawei","Vivo","Samsung","Oppo"]
    return text


# view all smartphones by brand
@app.route('/smartphones/<brand>', methods=['GET'])
def get_smartphone_by_brand(brand):
    """Returns all products by brand"""
    return jsonify(db.get_smartphone_by_brand(brand))


# view smartphone by name
@app.route('/smartphones/name/<brand>/<name>', methods=['GET'])
def get_smartphone_by_name(brand,name):
    """Returns a product by name"""
    return jsonify(db.get_smartphone_by_name(brand,name))


# view smartphone by price
@app.route('/smartphones/price/<brand>/<price>', methods=['GET'])
def get_smartphone_by_price(price,brand):
    """Returns a product by price"""
    return db.get_smartphone_by_price(price,brand)

# view add smartphone
@app.route('/smartphone/add', methods=['POST'])
def add_smartphone():
    """Adds a product to the database"""
    pass


# view delete smartphone
@app.route('/smartphone/delete/<brand>/<doc_id>') # methods=['DELETE'])
def delete_smartphone(doc_id,brand):
    """Deletes a product from the database"""
    db.delete_smartphone(doc_id,brand)
    return "removed"


if __name__ == '__main__':
    app.run(debug=True)