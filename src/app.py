from flask import Flask, jsonify
from dotenv import load_dotenv
from routes.auth import routes_auth

load_dotenv()

app = Flask(__name__)

app.register_blueprint(routes_auth)

@app.route('/', methods=['GET'])
def index():
    return jsonify ({'message': 'Welcomo to flash JWT API'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')