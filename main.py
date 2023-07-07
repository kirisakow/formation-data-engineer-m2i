import os
from flask import Flask, jsonify, request, Response
from pymongo import MongoClient

mongodb_port = 27017
app = Flask('my_flask_app')
mongo_client = MongoClient(
    os.environ.get('MONGO_HOST', ''),
    mongodb_port,
    username=os.environ.get('DB_ROOT_USERNAME', ''),
    password=os.environ.get('DB_ROOT_PASSWORD', '')
)
db = mongo_client[os.environ.get('DB_NAME', '')]
users = db.users

to_dict = lambda obj: {k: v for k, v in obj.items() if k in ['id', 'name', 'email']}

# users = [
#     {'id': 1, 'name': 'John Doe le papy', 'email': 'papy@doe.me'},
#     {'id': 2, 'name': 'John Doe le daron', 'email': 'daron@doe.me'},
#     {'id': 3, 'name': 'John Doe le jeune', 'email': 'jeune@doe.me'},
#     {'id': 4, 'name': 'Jane Doe la mamie', 'email': 'mamie@doe.me'},
#     {'id': 5, 'name': 'Jane Doe la daronne', 'email': 'daronne@doe.me'}
# ]


@app.route('/create_user', methods=['POST'])
@app.route('/create_user/', methods=['POST'])
def create_user():
    data = request.get_json()
    if data is None:
        return jsonify({'message': 'Cannot create a user: no data'}), 404
    user = {
        'id': users.find_one(sort=[('id', -1)])['id'] + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.insert_one(user)
    return jsonify([to_dict(u) for u in users.find()]), 201


@app.route('/', methods=['GET'])
@app.route('/users', methods=['GET'])
@app.route('/users/', methods=['GET'])
@app.route('/user', methods=['GET'])
@app.route('/user/', methods=['GET'])
def get_all_users():
    return jsonify([to_dict(u) for u in users.find()]), 200


@app.route('/user/<int:id>', methods=['GET'])
@app.route('/user/<int:id>/', methods=['GET'])
def get_user_by_id(id: int):
    if (user := users.find_one({'id': id})) is not None:
        return jsonify(to_dict(user)), 200
    return jsonify({'message': 'User not found'})


@app.route('/update_user/<int:id>', methods=['PUT'])
@app.route('/update_user/<int:id>/', methods=['PUT'])
def update_user(id: int):
    data = request.get_json()
    if data is None:
        return jsonify({'message': 'Cannot update a user: no data'}), 404
    user = {
        'id': data['id'],
        'name': data['name'],
        'email': data['email']
    }
    users.replace_one({'id': id}, user)
    return jsonify([to_dict(u) for u in users.find()]), 200


@app.route('/delete_user/<int:id>', methods=['DELETE'])
@app.route('/delete_user/<int:id>/', methods=['DELETE'])
def delete_user(id: int):
    if users.find_one({'id': id}) is not None:
        users.delete_one({'id': id})
        return jsonify([to_dict(u) for u in users.find()]), 200
    return jsonify({'message': 'User not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
