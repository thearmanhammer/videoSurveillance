import requests

while True:
	#r = requests.get('http://localhost:5000/text')
	#print('>>'+r.text)
	message = input('Message: ')
	r2 = requests.post('http://localhost:5000/text', data={'message':message})
	print(r2.text)