from controllers.signin import Signin
from controllers.login import Login
from controllers.buy import Buy
from controllers.sc import Sc

routes = {

    "signin":"/api/signin", "view_func_signin":Signin.as_view("api_signin"),
    "login":"/api/login", "view_func_login":Login.as_view("api_login"),
    "buy":"/api/buy", "view_func_buy":Buy.as_view("api_buy"),
    "sc":"/api/sc", "view_func_sc":Sc.as_view("api_sc")

}
