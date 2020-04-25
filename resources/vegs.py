import models

from flask import Blueprint

vegs = Blueprint('vegs', 'vegs')

@vegs.route('/')
def vegs_index():
	return 'vegs resource / blueprint working!'