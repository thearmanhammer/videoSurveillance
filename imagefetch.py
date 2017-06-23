from VideoCapture import Device
import time

cam = Device()

while(True):
	cam.saveSnapshot('image.jpg')