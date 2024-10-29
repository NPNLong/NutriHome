from flask import Flask
from flask_cors import CORS
from Recipes.controller  import recipes


def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.register_blueprint(recipes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)