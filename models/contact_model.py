from db_utils import db

class Contact:
    def __init__(self, nom, email, ident, area):
        self.nom = nom
        self.email = email
        self.ident = ident
        self.area = area

    def save(self):
        q = f"""INSERT INTO contactos (Nombre, Email, ident, area) 
                VALUES ('{self.nom}', '{self.email}', '{self.ident}', '{self.area}')"""
        cursor = db.cursor()
        cursor.execute(q)
        db.commit()