from flask import Flask, render_template, Response
from PIL import Image
import requests
import time

app = Flask(__name__)

#create default webpage with stream view
@app.route('/')
def index():
	return render_template('viewerhtml.html')

#the route where the images will be displayed
@app.route('/stream')
def stream():
	return Response(imageStream(), \
	mimetype='multipart/x-mixed-replace; boundary=frame')

#function which continually gets the image
def imageStream():
		#continually recieve and show image

	while True:
		#the image is recieved from the server
		r = requests.get('http://localhost:5000/feed')
		frame = r.content

		#display image
		yield (b' --frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

		#pause so computer doesnt fry
		time.sleep(0.01)

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)

	#tempchange