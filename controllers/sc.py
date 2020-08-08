from flask.views import MethodView
from flask import jsonify

class Sc(MethodView):

    def get(self):
        return 'Get-sc Complete', 200
