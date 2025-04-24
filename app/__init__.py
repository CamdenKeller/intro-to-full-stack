from flask import Flask, redirect, url_for, render_template
import os

def create_app():

    app = Flask(__name__, static_url_path='/static', static_folder='static')

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass  # or log the error if needed


    #set the database location
    app.config.from_mapping(
        SECRET_KEY = "dev",
        DATABASE = os.path.join(app.instance_path, "mydb.sqlite"),
    )

    from . import db
    db.init_app(app)

    from . import calculator
    app.register_blueprint(calculator.bp)

    # Redirect from "/" to "/calculate"
    @app.route("/")
    def index():
        return render_template("index.html")

    return app