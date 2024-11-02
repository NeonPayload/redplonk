from flask_login import UserMixin

from app import db


class user(db.Model, UserMixin):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True, autoincrement = True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    virustotal_key = db.Column(db.Text, nullable=True)
    shodan_key = db.Column(db.Text, nullable=True)
    # admin = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<user: {self.username}>'
    
    def get_id(self):
        return self.uid

    def get_virustotal_key(self):
        return self.virustotal_key

    def get_shodan_key(self):
        return self.shodan_key

class hosts(db.Model):
    __tablename__ = 'hosts'
    
    uid = db.Column(db.Integer, primary_key = True, autoincrement = True)
    hostname = db.Column(db.Text, nullable=True)
    ip_address = db.Column(db.Text, nullable=True)
    ports = db.Column(db.Text, nullable=True)
    vulns = db.Column(db.Text, nullable=True)
    shodan = db.Column(db.Text, nullable=True)
    whois = db.Column(db.Text, nullable=True)
    internetdb = db.Column(db.Text, nullable=True)

    