from flask import Flask, render_template, Response, request
from PIL import Image
import requests
import time
import datetime

app = Flask(__name__)

clip = None

#create default webpage with stream view
@app.route('/')
def index():
	return render_template('viewerhtml.html')

@app.route('/feed', methods=['GET', 'POST'])
def feed():
	if request.method == 'POST':
		print('POSTED')
		global clip
		clip = request.files['clip'].read()
		name = ('static/'+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
		clip.save(name)
		return clip
	if request.method == 'GET':
		return clip

@app.route('/content')
def content():
	return clip

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=6000, debug=True)

	#tempchange