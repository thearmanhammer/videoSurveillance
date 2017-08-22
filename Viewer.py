from flask import Flask, render_template, Response
from PIL import Image
import requests
import time

app = Flask(__name__)

#create default webpage with stream view
@app.route('/')
def index():
	return render_template('viewerhtml.html')

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=6000, debug=True)

	#tempchange