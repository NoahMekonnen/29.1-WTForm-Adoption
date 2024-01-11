from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, URLField, BooleanField,SelectField,IntegerField
from wtforms.validators import InputRequired, Optional, Email,NumberRange
class PetForm(FlaskForm):
    name = StringField("Name")
    species = SelectField("Species", choices =[('cat','cat'),('dog','dog'),('por','porcupine')])
    photo_url = URLField("Photo Url")
    age = IntegerField("Age",validators=[NumberRange(min=0,max=30)])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    photo_url = URLField("Photo Url")
    notes = StringField("Notes")
    available = BooleanField("Is the pet Available?")