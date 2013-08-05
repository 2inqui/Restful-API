__author__ = 'inqui'
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DATETIME)
    date_modified = db.Column(db.DATETIME)
    name = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    phone = db.Column(db.Text, unique=True)
    thumbnail_url = db.Column(db.Text)
    reg_id = db.Column(db.Text)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'            : self.id,
            'date_created'  : self.date_created,
            'date_modified' : self.date_modified,
            'name'          : self.name,
            'email'         : self.email,
            'phone'         : self.phone,
            'thumbnail_url' : self.thumbnail_url,
            'reg_id'        : self.reg_id
        }