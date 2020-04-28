from flask import Flask, jsonify
from resources.vegs import vegs
import models
from flask_cors import CORS

DEBUG=True
PORT=8000

app = Flask(__name__)

CORS(vegs, origins=['http://localhost:3000'], supports_credentials=True)
# blueprint
app.register_blueprint(vegs, url_prefix='/api/v1/vegs')

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



if __name__ == '__main__':
  models.initialize()
  app.run(debug=DEBUG, port=PORT)






