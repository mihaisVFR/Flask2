from flask import Flask, render_template, abort
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
BASE_DIR = Path(__file__).parent
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'main.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True)
    last_name = db.Column(db.String(50), unique=False)
    name = db.Column(db.String(50), unique=False)
    surname = db.Column(db.String(50), unique=False)
    birth_date = db.Column(db.Date, unique=False)
    phone = db.Column(db.String(50), unique=False)

    def __init__(self, login="", last_name="", name="", surname="", birth_date="", phone=""):
        self.login = login
        self.last_name = last_name
        self.name = name
        self.surname = surname
        date = datetime.strptime(birth_date, "%d/%m/%Y").date()
        self.birth_date = date
        self.phone = phone

    def to_dict(self):
        return {
            "login": self.login,
            "last_name": self.last_name,
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date.strftime("%d/%m/%Y"),
            "phone": self.phone,
            }


@app.route("/names")
def user_names():
    names = db.session.query(UserModel.name)
    entities = []
    for name in names:
        entities.append(*name)
    if names is None:
        return abort(404)
    return render_template("names.html",   entities=entities)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/table")
def table():
    entities = []
    names = UserModel.name
    surnames = UserModel.surname
    last_names = UserModel.last_name
    users = db.session.query(names, surnames, last_names).all()
    for user in users:
        entities.append({"last_name": user[2], "first_name": user[0], "surname": user[1]})
    return render_template("table.html", entities=entities)


@app.route("/users")
def users_list():
    entities = []
    users = UserModel.query.all()
    for user in users:
        entities.append(user.to_dict())
    return render_template("users_list.html", entities=entities)


@app.route("/users/<login>")
def user_item(login):
    entities = []
    users = UserModel.query.filter(UserModel.login == login)
    for user in users:
        if user is not None:
            entities.append(user.to_dict())
    if entities:
        return render_template("users_list.html", entities=entities)
    else:
        return f"User with login = {login} not found", 404


if __name__ == "__main__":
    app.run(debug=True)
