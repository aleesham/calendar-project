from flask import render_template, request, session
from app import app, db
from models import User

@app.route('/')
def index():
    return render_template('index.html', title = 'Test')

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        if False:
            ##TODO Verify information
            return redirect('/signup')
        else:
            ##This is supposing sign-up is successful
            return "Sign-Up Successful"

    return render_template('signup.html', title = 'Sign-Up')

if __name__ == '__main__':
    app.run()