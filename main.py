from flask import render_template, request, redirect, session, flash
from app import app, db
from models import User

@app.route('/')
def index():
    return render_template('index.html', title = 'Test')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify-password']
        num_of_errors = 0

        if len(username) < 3 or len(username) > 20:
            num_of_errors += 1
            flash('Username not valid.', 'error')
        if len(password) < 3 or len(password) > 20:
            num_of_errors += 1
            flash('Password not valid.', 'error')
        if password != verify_password:
            num_of_errors += 1
            flash('Passwords do not match.', 'error')
        

        if num_of_errors > 0:
            return redirect('/signup')
        else:
            session['username'] = username
            user = User(username, password)
            db.session.add(user)
            db.session.commit()
            return "Sign-Up Successful"

    return render_template('signup.html', title = 'Sign-Up')

app.secret_key = 'geJCtgNQcdPHJq9D'

if __name__ == '__main__':
    app.run()