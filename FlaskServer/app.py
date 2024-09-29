from flask import Flask

from FlaskServer.bp import mission_bp
from FlaskServer.db import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwii_missions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.register_blueprint(mission_bp)
app.run(debug=True)
