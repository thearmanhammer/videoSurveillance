import requests
from PIL import Image
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

def gen(camera):
	while True:
		time.sleep(0.001)
		r = requests.get('https://localhost:5000/video_feed')
		Image.open(io.BytesIO(r.content))
		yield (b'--frame\r\n'
			b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
	return Response(gen(Camera()),
		mimetype='multipart/x-mixed-replace; boundary=frame')