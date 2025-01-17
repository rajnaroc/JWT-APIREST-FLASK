from jwt import encode,decode
from jwt import exceptions
from os import getenv
from flask import jsonify
from datetime import datetime, timezone, timedelta
def write_token(data:dict):

    token = encode(payload={**data, 'exp': datetime.now(tz=timezone.utc) + timedelta(days=1)},key=getenv('SECRET'),algorithm='HS256')
    return token.encode('UTF-8')

def validar_token(token,output=False):
    try:
        if output:
            return decode(token,key=getenv('SECRET'), algorithms=["HS256"])
        
        decode(token,key=getenv('SECRET'), algorithms=['HS256'])
    except exceptions.DecodeError:
        reponse = jsonify({'message': 'Invalid Token'})
        reponse.status_code = 404
        
        return reponse
    except exceptions.ExpiredSignatureError:
        response = jsonify({'message': 'Token Token'})
        response.status_code = 404
        
        return response