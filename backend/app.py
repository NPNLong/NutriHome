from flask import Flask
from flask_cors import CORS
from Recipes.controller  import recipes
from Personal.controller import personal


def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.register_blueprint(recipes)
    app.register_blueprint(personal)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)