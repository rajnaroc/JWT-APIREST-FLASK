from flask import Blueprint, request
from requests import get
from function_jwt import validar_token


users_github = Blueprint('users_github', __name__)

@users_github.before_request
def verify_token_middleware():
    
    token = request.headers.get('Authorization').split(' ')[1]
    return validar_token(token)

@users_github.route('/github/users', methods=['POST'])
def get_users_github():
    
    data = request.get_json()
    country = data['country']

    response = get('https://api.github.com/search/users?q=location:{}'.format(country))

    return response.json()