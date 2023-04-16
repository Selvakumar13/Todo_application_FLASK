from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, validators
from flask_login import LoginManager

SECRET_KEY='some secret key'
app=Flask(__name__)
app.config['SECRET_KEY']=SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Users/DELL/todo/my_app/mydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

with app.app_context():
    db.create_all()
        
login_manager = LoginManager()
login_manager.init_app(app)

from my_app.api.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from my_app.api.views import todo
app.register_blueprint(todo)

from my_app.api.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


