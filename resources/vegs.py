import models

from flask import Blueprint

vegs = Blueprint('vegs', 'vegs')

# dont forget!  this is GET route (/api/v1/vegs)
@vegs.route('/', methods=['GET'])
def vegs_index():
	return 'vegs resource / blueprint working!'

# CREATE
# POST route /api/v1/vegs/ (don't forget slash at the end for POST)
@vegs.route('/', methods=['POST'])
def create_veg():
  return "hitting CREATE route!"

