from time import time
from VideoCapture import Device
from PIL import Image
import time

cam = Device()

class Camera(object):

	def __init__(self):
		self.frames = [open(f + '.jpg', 'rb').read() for f in['image']]

	def get_frame(self):
		self.frames = [open(f + '.jpg', 'rb').read() for f in['image']]
		return self.frames[0]