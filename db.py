from tinydb import TinyDB, Query
from flask import  jsonify


class SmartphoneDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
    
    def brands(self):
        """Returns all brands in the database"""
        a=[]
        b=["Apple","Huawei","Oppo","Samsung","Nokia","Vivo","Redmi"]
        for i in b:
            a+=self.db.table(i).all()
        return a
    
    def get_smartphone_by_brand(self, brand):
        """Returns all products by brand"""
        return self.db.table(brand).all()
    
    def get_smartphone_by_name(self,brand,name):
        """Returns a product by name"""
        data=self.db.table(brand)
        return data.search(self.query.name==name)

    def get_smartphone_by_price(self, price):
        """Returns a product by price"""
        pass
    
    def add_smartphone(self, smartphone, brand):
        """Adds a product to the database"""
        pass
    
    def delete_smartphone(self, doc_id, brand):
        """Deletes a product from the database"""
        pass
db=SmartphoneDB("db.json")
    
if __name__=="__db.py__":
    print(db.brands())