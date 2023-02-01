from config import *

class User(db.Model):
    userid = db.Column('user_id',db.Integer(),primary_key=True)
    name = db.Column('user_name',db.String(50),unique=True)
    email = db.Column('user_email',db.String(50),unique=True)
    password= db.Column('user_pass',db.String(50))



with app.app_context():
    db.create_all()
    print('Tables created...')

