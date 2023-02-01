from flask import Flask,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ram123@localhost/flaskdb1'
#app.config['SQLALCHEMY_ECHO'] = True
db=SQLAlchemy(app)