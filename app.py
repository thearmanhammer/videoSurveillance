from flask import Flask, render_template, Response, request
from PIL import Image

app = Flask(__name__)

#declare image variable so it is accessible everywhere
pic = None

#create default blank webpage
@app.route('/')
def index():
	return render_template('serverhtml.html')	

#create route where image is recieved and held and can be accessed
@app.route('/feed', methods=['GET', 'POST'])
def feed():

	#on POST, aka when something is sent, recieve and return image
	if request.method == 'POST':
		global pic
		pic = request.files['picture'].read()
		return pic

	#on GET, aka when something is retrieved, return current image
	elif request.method == 'GET':
		return pic

	#a method which shouldnt be called is being called on the server
	else:
		#let the user know
		print('Error: '+request.method+'has been called')
		return ('Error: '+request.method+'has been called')

#the route where the stream is located
@app.route('/stream')
def stream():
	return Response(imageStream(), \
	mimetype='multipart/x-mixed-replace; boundary=frame')

#function which continually gets the image
def imageStream():

		#continually show image
	while True:

		#display image
		yield (b' --frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + pic + b'\r\n')

		#pause so computer doesn't fry
		time.sleep(0.01)

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)