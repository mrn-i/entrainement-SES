from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField, SelectField, FieldList
from wtforms.validators import DataRequired

grouplist = [("Group1", "Groupe 1"), ("Group2", "Groupe 2")]

class WordForm(FlaskForm):
    word = StringField('......', [DataRequired()])

class SalaryForms(FlaskForm):
    yearsofexperience = IntegerField('years', validators=[DataRequired()])

class AnswerForms(FlaskForm):
    nom = StringField('Nom', [DataRequired()])
    prenom = StringField('Prénom', [DataRequired()])
    groupe = SelectField('Groupe', choices = grouplist)

    word1 = StringField('......', [DataRequired()])
    word2 = StringField('......', [DataRequired()])
    word3 = StringField('......', [DataRequired()])
    word4 = StringField('......', [DataRequired()])
    word5 = StringField('......', [DataRequired()])
    word6 = StringField('......', [DataRequired()])
    word7 = StringField('......', [DataRequired()])
    word8 = StringField('......', [DataRequired()])
    word9 = StringField('......', [DataRequired()])
    word10 = StringField('......', [DataRequired()])
    word11 = StringField('......', [DataRequired()])
    word12 = StringField('......', [DataRequired()])
    word13 = StringField('......', [DataRequired()])
    word14 = StringField('......', [DataRequired()])
    word15 = StringField('......', [DataRequired()])
    word16 = StringField('......', [DataRequired()])
    word17 = StringField('......', [DataRequired()])
    word18 = StringField('......', [DataRequired()])

    submit = SubmitField('Envoyez vos réponses')

class AnswerForms2(FlaskForm):
    nom = StringField('Nom', [DataRequired()])
    prenom = StringField('Prénom', [DataRequired()])
    words = FieldList(StringField('....', [DataRequired()]), min_entries=0, max_entries=20)
    submit = SubmitField('Submit')