import json

from flask import Blueprint

test_api = Blueprint( 'test_api', __name__ )

@test_api.route( '/' )
def test():
    return json.dumps( { 'message': 'Hello World!' } )