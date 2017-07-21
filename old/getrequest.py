import requests
from PIL import Image
from flask import Flask, render_template, Response
import time
import io
from reccamera import RecieveCamera

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('getindex.html')

def gen(camera):
	while True:
		time.sleep(0.001)
		frame = camera.get_frame()
		yield (b' --frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen(RecieveCamera()),
		mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000, debug=True)