from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

import os
app = Flask(__name__)
app.config['SECRET_KEY'] = "231Asdasdasda232asda"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/manish_mandot"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
login_manager.login_view = 'admin.Login'
ma= Marshmallow(app)

db = SQLAlchemy(app)
Migrate(app,db)
from application.Admin.routes import admin
app.register_blueprint(admin)
from application.Apis.routes import apis
app.register_blueprint(apis,url_prefix='/apis')