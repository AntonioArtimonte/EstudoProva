from tinydb import TinyDB, Query

class Database:
    def __init__(self, db_path):
        self.db = TinyDB(db_path)
        self.query = Query()
        
    def add_registry(self, registry):
        return self.db.insert({'item': registry})
    
    def get_all_registrations(self):
        return self.db.all()
    
    def get_registration_by_id(self, id):
        return self.db.get(doc_id=id)
    
    def update_registration(self, id, registry):
        return self.db.update({'item': registry}, doc_ids=[id])
    
    def delete_registration(self, id):
        return self.db.remove(doc_ids=[id])
    
