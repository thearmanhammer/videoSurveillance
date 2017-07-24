from time import time
#from VideoCapture import Device
from PIL import Image
import time
import cv2

class Camera(object):

	def __init__(self):
		self.cam = cv2.VideoCapture(0)
		pic = self.cam.read()[1]
		cv2.imwrite('image.jpg', pic)
		self.frames = [open(f + '.jpg', 'rb').read() for f in ['image']]

	def get_frame(self):
		pic = self.cam.read()[1]
		cv2.imwrite('image.jpg', pic)
		self.frames = [open(f + '.jpg', 'rb').read() for f in ['image']]
		return self.frames[0]