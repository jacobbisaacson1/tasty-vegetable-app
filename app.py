from flask import Flask, jsonify
from resources.vegs import vegs
from resources.users import users
import models
from flask_cors import CORS
from flask_login import LoginManager

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = "super secret pizza party."
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  try:
    return models.User.get(user_id)
  except models.DoesNotExist:
    return None

CORS(vegs, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
# blueprint
app.register_blueprint(vegs, url_prefix='/api/v1/vegs')
app.register_blueprint(users, url_prefix='/api/v1/users')

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






