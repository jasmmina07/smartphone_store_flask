from tinydb import TinyDB, Query


class SmartphoneDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
    
    def get_all_brands(self):
        """Returns all brands in the database"""
        return self.db.all()
    
    def get_all_products_by_brand(self, brand):
        """Returns all products by brand"""
        return self.db.search(self.query.brand == brand)
