import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

vegs = Blueprint('vegs', 'vegs')

# dont forget!  this is GET route (/api/v1/vegs)
@vegs.route('/', methods=['GET'])
def vegs_index():
  result = models.Veg.select().dicts()
  # veggies = [veg.name for veg in result]
  print('this is result -->', result)
  return jsonify(
    data = [veg for veg in result],
    message = 'Getting Veggies',
    status = 200
  )

# CREATE
# POST route /api/v1/vegs/ (don't forget slash at the end for POST)
@vegs.route('/', methods=['POST'])
def create_veg():
  payload = request.get_json()
  print(payload)
  new_veg = models.Veg.create(
    name=payload['name'], 
    color=payload['color'], 
    isTasty=payload['isTasty']
  )
  print(new_veg)
  print(new_veg.__dict__)
  print(dir(new_veg))
  veg_dict = model_to_dict(new_veg)
  return jsonify(
    data=veg_dict,
    message="created(post) veg",
    status=201
  ), 201

# Destroy
@vegs.route('/<id>', methods=['DELETE'])
def delete_veg(id):
  delete_query = models.Veg.delete().where(models.Veg.id == id)
  num_of_rows_deleted = delete_query.execute()
  print(num_of_rows_deleted)
  return jsonify(
    data={},
    message="successfully deleted {} veg with id {}".format(num_of_rows_deleted, id),
    status=200
  ), 200

# Update 
# @vegs.route('/<id>', methods)

  

