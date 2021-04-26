from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from Resources.ItemResouce import ItemResource, PostItemResource

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///thisismydb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.secret_key = 'london'
api = Api(app)
api.add_resource(ItemResource, '/item/<int:itemId>')
api.add_resource(PostItemResource, '/item')

@app.before_first_request
def create_tables():
    db.create_all()

db.init_app(app)
app.run(host='0.0.0.0', port=5000, debug=True)
