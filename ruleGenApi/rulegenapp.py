#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
from ruleGenLogic import gen_rules

app = Flask(__name__)
auth = HTTPBasicAuth()

# bad practice username should not be stored in clear text
@auth.get_password
def get_password(username):
    if username == 'rule':
        return 'gen'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)



@app.route('/ruleGen/api/v1.0/rules/<string:data>', methods=['GET'])
@auth.login_required
def rules(data):
    rules = gen_rules(data)
    return rules

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)