from flask import render_template, request, session
from app import app, db

@app.route('/')
def index():
    return render_template('index.html', title = 'Test')

if __name__ == '__main__':
    app.run()