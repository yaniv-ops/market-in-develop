from flask import Flask
from flask_bootstrap import Bootstrap4



app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///stock.db"
#app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:shafita77@localhost/stock"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap4(app)
