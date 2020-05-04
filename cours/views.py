#!/usr/bin/env python3

from flask import Flask, render_template, url_for,	 request

import os


os.environ["APP_SETTINGS"] = "config.ProductionConfig"

app = Flask(__name__)
#Permet d'importer toutes les variables de configuration
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config.from_object("config.DevelopmentConfig")
# app.config['SQLALCHEMY_ECHO'] = True
#app.config.from_object(os.environ.get('APP_SETTINGS', DevelopmentConfig))

app.config.from_object(os.environ["APP_SETTINGS"])
app.secret_key = 'development key' # Flask_WTform CSFR protection

from .templates.includes.forms import AnswerForms, AnswerForms2


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cours_ch6")
def ch6():
    return render_template("Chapitre 6.html")

@app.route("/cours_ch7")
def ch7():
    return render_template("Chapitre 7.html")


