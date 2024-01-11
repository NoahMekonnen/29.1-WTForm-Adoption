from flask import Flask, request, redirect, render_template, flash, session
from models import db, connect_db, Pet
from flask_debugtoolbar import DebugToolbarExtension
from forms import EditPetForm, PetForm

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Users2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Godalone1."
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.drop_all()
db.create_all()

@app.route('/')
def show_pets():
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    form = PetForm()
    print(form, "this is the value")
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        print("HEYYYYYYYYYYYY")
        return render_template('add_pet.html',form=form)
    
@app.route('/<int:pet_id>', methods=['GET','POST'])
def detail(pet_id):
    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        raise
        return render_template('pet_detail.html',pet=pet,form=form)


