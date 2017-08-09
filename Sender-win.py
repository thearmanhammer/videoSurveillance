from VideoCapture import Device
from PIL import Image
import requests
import time

#generate a camera to take picture using local device
cam = Device()

#send picture to local server
def post(picture):

	#post request to send image as a file
	#r = requests.post('http://localhost:5000/feed', files={'picture':picture})
	r = requests.post('https://obscure-dusk-57827.herokuapp.com/feed', files={'picture':picture})

	#let the user know that the image has been posted
	print('posted')

#continually take pictures
while True:

	#capture picture initially
	pic = cam.getImage()

	#convert to a sendable file
	finalpic = open("image.jpeg", 'rb')

	#post the picture
	r = requests.post('https://obscure-dusk-57827.herokuapp.com/feed', files={'picture':finalpic})
	#r = requests.post('http://localhost:5000/feed', files={'picture':finalpic})

	#close photo so it can be replaced
	finalpic.close()

	#notify the user
	print('posted')

	#pause so computer doesn't fry
	time.sleep(0.01)