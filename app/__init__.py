from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

# Loading the .env file
load_dotenv()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    CORS(app)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    from .models.cars import Car
    from .models.drivers import Driver

    from .routes.cars import cars_bp
    app.register_blueprint(cars_bp)

    from .routes.drivers import drivers_bp
    app.register_blueprint(drivers_bp)

    return app


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# # Creating a new SQLAlchemy object
# # Created outside the create_app so we can import db to other files
# db = SQLAlchemy()
# migrate = Migrate()


# # create_app() is called by Flask when we run: 'flask run' 
# def create_app():
#     # __name__ stores the name of the module we're in
#     app = Flask(__name__)

#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#     # Telling SQLAlchemy where our Postgres is and this is the database I want to use
#     app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:postgres@localhost:5432/hello_cars_development"

#     # Connecting our db and app
#     db.init_app(app)
#     migrate.init_app(app, db)

#     # If you import this at the top of the file, you'll get errors
#     # Getting our blueprint
#     from .models.cars import cars_bp
#     # Registering the blueprint
#     app.register_blueprint(cars_bp)

#     return app