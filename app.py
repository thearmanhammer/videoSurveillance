from flask import Flask, flash, redirect, render_template, request, session, abort
from PIL import Image
import time
import datetime
import os

app = Flask(__name__)

clip = None
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('viewerhtml.html')
 
@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route('/feed', methods=['GET', 'POST'])
def feed():
    if request.method == 'POST':
        print('POSTED')
        global clip
        clip = request.files['clip'].read()
        name = ('static/'+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        # clip.save(name)
        return clip
    if request.method == 'GET':
        return clip

@app.route('/content')
def content():
    return clip

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)