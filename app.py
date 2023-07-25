import os

from flask_bcrypt import Bcrypt
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms.reservation_form import ReservationForm
from forms.daily_menu_edit_form import EditForm
from os import path
import json

app = Flask(__name__)

# Configure the database connection URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food.db'
app.config['SECRET_KEY'] = 'your_secret_key'

# Create an instance of the SQLAlchemy class
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

hashed_password = bcrypt.generate_password_hash('test').decode('utf-8')


from models.reservation import Reservation


@app.route("/", methods=['POST', 'GET'])
def home_page():
    form = ReservationForm()

    if form.validate_on_submit():
        reservation = Reservation(
            reservation_date=form.reservation_date.data,
            reservation_time=form.reservation_time.data,
            num_guests=form.num_guests.data,
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data
        )
        db.session.add(reservation)
        db.session.commit()
        return redirect(url_for('registration_created'))

    return render_template("index.html", form=form)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password')

        if bcrypt.check_password_hash(hashed_password, password):
            return render_template("admin.html")
        else:
            return "Invalid password"

    return render_template('login.html')


@app.route('/daily_menu', methods=['GET', 'POST'])
def daily_menu():
    with open('data/daily_menu_data.json', 'r') as json_file:
        menu_data = json.load(json_file)
    return render_template('daily_menu.html', menu_data=menu_data)


@app.route("/registration_created")
def registration_created():
    return render_template("registration_created.html")


@app.route('/change_daily_menu', methods=['GET', 'POST'])
def change_daily_menu():
    menu_forms = []

    with open('data/daily_menu_data.json', 'r') as json_file:
        menu_data = json.load(json_file)

    edit_form = EditForm()

    for category, items in menu_data.items():
        for item in items:
            form = EditForm()
            form.id.data = item['id']  # Populate the 'id' field of the form
            form.mnozstvi.data = item['mnozstvi']
            form.jidlo.data = item['jidlo']
            form.alergeny.data = item['alergeny']
            form.cena.data = item['cena']
            menu_forms.append((category, form))

    if request.method == 'POST':
        print("Form is valid and submitted.")
        print(request.form)

        for category, form in menu_forms:
            field_prefix = f"{category}_{form.id.data}_"
            if form.validate_on_submit():
                # Update the item with the form data
                item_to_update = next((item for item in menu_data[category] if item['id'] == form.id.data), None)
                if item_to_update:
                    item_to_update['mnozstvi'] = request.form.get(f"{field_prefix}mnozstvi")
                    item_to_update['jidlo'] = request.form.get(f"{field_prefix}jidlo")
                    item_to_update['alergeny'] = request.form.get(f"{field_prefix}alergeny")
                    item_to_update['cena'] = request.form.get(f"{field_prefix}cena")

        print("Před ukládáním:", menu_data)

        # Ukládání dat do souboru
        with open('data/daily_menu_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(menu_data, json_file, indent=4, ensure_ascii=False)

        # Po ukládání do souboru
        print("Po ukládáním:", menu_data)

        return redirect(url_for('change_daily_menu'))

    return render_template('change_daily_menu.html', menu_forms=menu_forms)

if __name__ == '__main__':
    # Check if the database file exists
    if not path.exists("food.db"):
        with app.app_context():
            db.create_all()

    app.run()
