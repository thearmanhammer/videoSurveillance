from VideoCapture import Device
from PIL import Image
from io import BytesIO
import requests
import time

#generate a camera to take picture using local device
cam = Device()

#send picture to local server
def post(picture):

	#post request to send image as a file
	r = requests.post('http://localhost:5000/feed', data={'picture':picture})

	#let the user know that the image has been posted
	print('posted')

#continually take pictures
while True:

	#capture picture initially
	pic = cam.getImage()
	print('.   ')

	#convert to a sendable file 'img'
	img = BytesIO()
	pic.save(img, 'JPEG')
	img.seek(0)

	#send image to send function
	print(img)
	post(pic)

	#pause so computer is not fry
	time.sleep(0.01)