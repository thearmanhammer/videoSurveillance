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

#the route where the images will be displayed
@app.route('/stream')
def stream():
	return Response(imageStream(), \
	mimetype='multipart/x-mixed-replace; boundary=frame')

#function which continually gets the image
def imageStream():
		#continually recieve and show image
	while True:
		#the image is recieved from the server as a bytesio file
		r = requests.get('http://localhost:5000/feed')
		# bimg = BytesIO(r.content)
		# bimg.seek(0)

		print(r.content)

		#convert bytesio to image
		# img = BytesIO()
		# img = r.content
		# print(type(r.content))
		# print(dir(r.content))
		# pic.save(img, "JPEG")

		#display image
		yield (b' --frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + r.content + b'\r\n')

		#pause so computer doesnt fry
		time.sleep(0.01)

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)