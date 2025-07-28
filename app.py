from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'zxcvbnm'

def init_db():
    if not os.path.exists('users.db'):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL, gender TEXT NOT NULL, dob TEXT NOT NULL, phone_number TEXT NOT NULL)''')
        conn.commit()
        conn.close()
init_db()

@app.route('/')
def home():
    return redirect(url_for('login'))
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE email = ?',(email,))
        user = c.fetchone()
        conn.close()

        if user and check_password_hash(user[3], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login Successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials. Try Again!!', 'error')
    return render_template('login.html')
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        gender = request.form['gender']
        dob = request.form['dob']
        phone_number = request.form['phone_number']

        if password != confirm_password:
            flash('Passwords do not match!!', 'error')
            return render_template('signup.html')
        
        hashed_pw = generate_password_hash(password)

        try:
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('INSERT INTO users (username, email, password, gender, dob, phone_number) VALUES (?, ?, ?, ?, ?, ?)', (username, email, hashed_pw, gender, dob, phone_number))
            conn.commit()
            conn.close()
            flash('SignUp Successfull! Please Login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email Already Exists!!', 'error')
    return render_template('signup.html')
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please Login first!!', 'error')
        return redirect(url_for('login'))
    flash(f"Welcome, {session['username']}! <a href='/logout'>Logout</a>", 'success')
    return render_template('index.html')
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out Successfully', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)