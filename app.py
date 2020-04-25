# from flask import Flask
from flask import Flask, jsonify

DEBUG=True
PORT=8000

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, world'

@app.route('/veg_json')
def get_veg_json():
	return jsonify(name="Carrot", color="Orange", isTasty=True)

@app.route('/nested_json')
def get_nested_json():
	carrot = {
		'name': 'Carrot',
		'color': 'Orange',
		'isTasty': True
	}
	return jsonify(name="Jacob", likesVeg=True, veg=carrot)


@app.route('/likes_veg/<username>')
def likes_veg(username):
	return "You better like vegetables {}!".format(username)






















# DONT FORGOT TO pip install Flask !!!!!

if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)