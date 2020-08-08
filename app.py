from flask import Flask
from routes import *

app = Flask(__name__)

# Routes
app.add_url_rule(routes["signin"], view_func=routes["view_func_signin"])
app.add_url_rule(routes["login"], view_func=routes["view_func_login"])
app.add_url_rule(routes["buy"], view_func=routes["view_func_buy"])
app.add_url_rule(routes["sc"], view_func=routes["view_func_sc"])

