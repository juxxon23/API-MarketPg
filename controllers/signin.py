from flask.views import MethodView
from flask import request, json
from validators.user import UserSchema 
from helpers.encrypt_pass import EncryptPass

user_schema = UserSchema()
encrypt_passw = EncryptPass()

class Signin(MethodView):
   
    def post(self):
        errors = user_schema.validate(request.form)
        if errors:
           return errors, 400
        else:
            user = request.form['user_sign']
            email = request.form['email_sign'] 
            hash_pass = encrypt_passw.do(request.form['pass_sign'])       
            users = {user:{'email':email, 'password':hash_pass}}
            with open('data/users.json', 'w') as outfile:
                json.dump(users, outfile, indent=2)
                return 'Complete', 200
        return 'Finished', 200

                          
