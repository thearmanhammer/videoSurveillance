from flask import Flask, render_template, Response
from io import BytesIO
from PIL import Image
import requests
import time

app = Flask(__name__)

#create default webpage with stream view
@app.route('/')
def index():
	return render_template('viewerhtml.html')

#the route where the images will be recieved and displayed
@app.route('/stream')
def stream():
	#continually recieve and show image
	while True:
		#the image is recieved from the server as a bytesio file
		r = requests.get('http://localhost:5000/feed')
		bimg = BytesIO(r.content)

		#convert bytesio to image
		img = Image.open(bimg)

		#display newfound image
		yield (b' --frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')

		#pause so computer doesnt fry
		time.sleep(0.01)

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)