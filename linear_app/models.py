#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from .views import app
import datetime as dt

db = SQLAlchemy(app)

class Result(db.Model):
    __tablename__ = "LinRegResults"

    id = db.Column(db.Integer, primary_key = True)  
    YearsExperience = db.Column(db.Float)
    Prediction = db.Column(db.Float)

    def __init__(self, YearsExperience, Prediction):
        self.YearsExperience = YearsExperience
        self.Prediction = Prediction

    def __repr__(self):
        return '<id {}>'.format(self.id)

class SaveTest(db.Model):
    __tablename__ = "Test_SES"

    id = db.Column(db.Integer, primary_key = True)
    prenom = db.Column(db.String(200))
    nom = db.Column(db.String(200))
    groupe = db.Column(db.String(200))
    exercice = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=dt.datetime.now())
    answer = db.Column(db.String(500))

    def __init__(self, prenom, nom, groupe, answer, exercice):
        self.prenom = prenom
        self.nom = nom
        self.groupe = groupe
        self.answer = answer
        self.exercice = exercice



    def __repr__(self):
        return '<id {}>'.format(self.id)