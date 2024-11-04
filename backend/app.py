from flask import Flask
from Login_Signup.controller import auth_bp
from Home.controller import calorie_bp
from Weekly_menu.controller import menu_bp
from Family.controller import family_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(calorie_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(family_bp)
    return app 


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)