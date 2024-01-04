from flask import Flask
from routes import routes
from atom import Atom

app = Flask(__name__)
app.register_blueprint(routes)
atom_server = Atom(app)