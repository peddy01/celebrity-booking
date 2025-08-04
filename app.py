from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    celebrity = db.Column(db.String(100))
    event_type = db.Column(db.String(100))
    date = db.Column(db.String(50))
    location = db.Column(db.String(150))
    budget = db.Column(db.String(50))
    status = db.Column(db.String(50), default='Pending')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        data = Booking(
            name=request.form['name'],
            email=request.form['email'],
            celebrity=request.form['celebrity'],
            event_type=request.form['event_type'],
            date=request.form['date'],
            location=request.form['location'],
            budget=request.form['budget']
        )
        db.session.add(data)
        db.session.commit()
        return render_template('confirmation.html', name=data.name)
    return render_template('book.html')

@app.route('/admin')
def admin():
    bookings = Booking.query.all()
    return render_template('admin/dashboard.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
