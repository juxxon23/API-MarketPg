from flask.views import MethodView
from flask import request
from helpers.load_json import JsonManager
from helpers.bought import Bought

bought_var = Bought()
manager = JsonManager()
products_list = manager.load_json("data/products.json")

class Buy(MethodView):
 
    def get(self):
        return products_list, 200
    
    def post(self):
        categoria = request.form["categorie"]
        cantidad = int(request.form["num"])
        status = bought_var.save(products_list, categoria, cantidad), 200
        return status
   
