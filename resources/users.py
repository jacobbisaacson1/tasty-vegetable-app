import models
from flask import Blueprint, request
users = Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def test_user_resource():
	return "user ref works"

@users.route('/register', methods=['POST'])
def register():
	print(request.get_json())
	return "see terminal"