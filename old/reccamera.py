from time import time
from PIL import Image
import time
from io import BytesIO
import requests

class RecieveCamera(object):

	def __init__(self):
		r = requests.get('http://localhost:5000/video_feed', timeout=30)
		i = Image.open(BytesIO(r.content))

	def get_frame(self):
		r = requests.get('http://localhost:5000/video_feed', timeout=30)
		i = Image.open(BytesIO(r.content))
