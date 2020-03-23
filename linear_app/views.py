#!/usr/bin/env python3

from flask import Flask, render_template, url_for,	 request
from sklearn.externals import joblib
from numpy import round
from config import DevelopmentConfig, ProductionConfig
import os

'''
# Pour figer les variables d'environnement en DEVELOPPEMENT
os.environ["APP_SETTINGS"] = "config.DevelopmentConfig"
os.environ['DBUSER'] = "postgres"
os.environ['DBPASS'] = "azeR1234"
os.environ['DBHOST'] = "localhost"
os.environ['DBNAME'] = "postgres"
'''
'''
#Pour figer les variables d'environnement en PRODUCTION
os.environ["APP_SETTINGS"] = "config.ProductionConfig"
os.environ['DBUSER'] = "zfjgsayxgjeago"
os.environ['DBPASS'] = "a46aab50bd8ff8d9585a5c3aae90143e4ff93f9e993b7c1c31524b84748175af"
os.environ['DBHOST'] = "ec2-54-247-169-129.eu-west-1.compute.amazonaws.com"
os.environ['DBNAME'] = "dohirlotb7iqt"
'''

os.environ["APP_SETTINGS"] = "config.DevelopmentConfig"

app = Flask(__name__)
#Permet d'importer toutes les variables de configuration
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config.from_object("config.DevelopmentConfig")
# app.config['SQLALCHEMY_ECHO'] = True
#app.config.from_object(os.environ.get('APP_SETTINGS', DevelopmentConfig))

app.config.from_object(os.environ["APP_SETTINGS"])
app.secret_key = 'development key' # Flask_WTform CSFR protection

from .models import Result, SaveTest
from .models import db
from .templates.includes.forms import AnswerForms, AnswerForms2

@app.before_request
def before_request():
    """Connect to the database before each request."""
    # g = global object Flask uses for passing information to views/modules.
    # g.db = db
    # g.db.connect()
    pass

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    # g.db.close()
    return response


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/test1", methods=('GET', 'POST'))
def test1():
    form = AnswerForms()

    if request.method == "POST":
        keylist = [("word" + str(x)) for x in range(1,15)]
        student_answers = [form.data[x] for x in keylist]

        result = SaveTest(
            nom=str(dict(request.form)["nom"]),
            prenom=str(dict(request.form)["prenom"]),
            groupe=str(dict(request.form)["groupe"]),
            answer=[form.data[x] for x in keylist],
            exercice = 'Synthese 2A'
        )

        db.session.add(result)
        db.session.commit()
        app.logger.info(result.id)

        return render_template("answer1.html", prop = student_answers)

    else :
        return render_template("test1.html", form = form)


@app.route("/test2", methods=('GET', 'POST'))
def test2():
    form = AnswerForms()

    if request.method == "POST":
        keylist = [("word" + str(x)) for x in range(1, 17)]
        student_answers = [form.data[x] for x in keylist]

        result = SaveTest(
            nom=str(dict(request.form)["nom"]),
            prenom=str(dict(request.form)["prenom"]),
            groupe=str(dict(request.form)["groupe"]),
            answer=[form.data[x] for x in keylist],
            exercice='Synthese 2B'
        )

        db.session.add(result)
        db.session.commit()
        app.logger.info(result.id)

        return render_template("answer2.html", prop=student_answers)

    else:
        return render_template("test2.html", form=form)

@app.route("/test3", methods=('GET', 'POST'))
def test3():
    form = AnswerForms()

    if request.method == "POST":
        keylist = [("word" + str(x)) for x in range(1,18)]
        student_answers = [form.data[x] for x in keylist]

        result = SaveTest(
            nom=str(dict(request.form)["nom"]),
            prenom=str(dict(request.form)["prenom"]),
            groupe=str(dict(request.form)["groupe"]),
            answer=[form.data[x] for x in keylist],
            exercice = 'Synthese 2C'
        )

        db.session.add(result)
        db.session.commit()
        app.logger.info(result.id)

        return render_template("answer3.html", prop = student_answers)

    else :
        return render_template("test3.html", form = form)


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":
        regressor = joblib.load("./linear_regression_model.pkl")
        yearsExperience = [[float(dict(request.form)["YearsExperience"])]]
        prediction = (regressor.predict(yearsExperience)/100)*100

        result = Result(
            YearsExperience = yearsExperience[0][0],
            Prediction = float(prediction)
        )

        db.session.add(result)
        db.session.commit()


    return render_template("prediction.html", prediction = int(prediction), YearsExperience = int(yearsExperience[0][0]))


