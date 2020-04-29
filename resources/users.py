import models 

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash

users = Blueprint('users', 'users')
@users.route('/', methods=['GET'])
def test_user_resource(): 
  return "user resource works"

@users.route('/register', methods=['POST'])
def register():
  print(request.get_json())
  payload = request.get_json()
  payload['email'] = payload['email'].lower()
  payload['username'] = payload['username'].lower()
  print(payload)


  try:
    models.User.get(models.User.email == payload['email'])
    return jsonify(
      data={},
      message="A user with that email already exists",
      status=401
    ), 401
  except models.DoesNotExist:
    pw_hash = generate_password_hash(payload['password'])
    created_user = models.User.create(
      username=payload['username'],
      email=payload['email'],
      password=pw_hash
    )

    print(created_user)

  return "check terminal"