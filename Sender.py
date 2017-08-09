import cv2
from PIL import Image
import requests
import time

class A():
	def __init__(self):
		self.video = cv2.VideoCapture(0)
		bytes=''
		#continually take pictures
		while True:
			success, pic = self.video.read()
			ret, jpg = cv2.imencode('.jpg', pic)
			post(jpg)

			#pause so computer doesn't fry
			time.sleep(0.001)

def post(picture):

	#post request to send image as a file
	r = requests.post('http://localhost:5000/feed', data={'picture':picture})

	#let the user know that the image has been posted
	print('posted')

a = A()