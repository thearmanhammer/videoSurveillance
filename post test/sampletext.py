from flask import Flask, render_template, Response, request
from io import StringIO

app = Flask(__name__)
msg = 'string'

@app.route('/')
def index():
	return render_template('temptemplate.html')

@app.route('/text', methods=['GET', 'POST'])
def text():
	if request.method == 'POST':
		global msg
		msg = request.form['message']
		print(msg)
		return msg
	elif request.method == 'GET':
		return msg
	else:
		return 'hello world'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)