from flask import Flask, render_template, Response, request
from PIL import Image
import time
from time import gmtime, strftime

app = Flask(__name__)

#declare image variable so it is accessible everywhere
clip = None

#create default blank webpage
@app.route('/')
def index():
	return render_template('vidindex.html')	

#create route where image is recieved and held and can be accessed
@app.route('/feed', methods=['GET', 'POST'])
def feed():

	#on POST, aka when something is sent, recieve and return image
	if request.method == 'POST':
		print('pob1')
		global clip
		print('pob2')
		clip = request.files['clip']
		currenttime = (strftime("%Y-%m-%d %H:%M:%S", gmtime())+'.mp4')
		print('pob3')
		clip.save(os.path.join(app.config['UPLOAD_FOLDER'], currenttime))
		return clip

	#on GET, aka when something is retrieved, return current image
	elif request.method == 'GET':
		return clip

	#a method which shouldnt be called is being called on the server
	else:
		#let the user know
		print('Error: '+request.method+'has been called')
		return ('Error: '+request.method+'has been called')

#the route where the stream is located
@app.route('/stream')
def stream():
	return Response(imageStream(),
		mimetype='multipart/x-mixed-replace; boundary=frame')

#function which continually gets the image
def imageStream():

	#continually show image
	while True:
		#display image
		#print('yielding')
		yield (clip)
		#pause so computer doesn't fry

#where the app will run and be hosted
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)