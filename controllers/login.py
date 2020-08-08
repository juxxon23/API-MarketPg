from flask.views import MethodView
from flask import request, json
import bcrypt

class Login(MethodView):

    def post(self):
        user = request.form['user_login']
        password = request.form['pass_login'].encode('utf-8')
        with open('data/users.json') as json_file:
            data = json.load(json_file)
            if data.get(user):
                pass_db = data[user]['password']
                if bcrypt.checkpw(password, pass_db.encode('utf-8')): 
                    return 'welcome', 200
                return 'Incorrect password', 400
            return 'Incorrect user', 400
        return 'Complete', 200
        
