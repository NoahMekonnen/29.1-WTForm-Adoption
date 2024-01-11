from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
class PetForm(FlaskForm):
    name = StringField("Name")
    species = StringField("Species")
    photo_url = StringField("Photo Url")
    age = StringField("Age")
    Notes = StringField("Notes")