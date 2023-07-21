
from flask_bcrypt import Bcrypt
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms.reservation_form import ReservationForm
from os import path

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
            return "Welcome to the admin page!"
        else:
            return "Invalid password"

    return render_template('login.html')


@app.route("/registration_created")
def registration_created():
    return render_template("registration_created.html")


if __name__ == '__main__':
    # Check if the database file exists
    if not path.exists("food.db"):
        with app.app_context():
            db.create_all()

    app.run()
