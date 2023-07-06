from flask import Flask, jsonify, request

app = Flask('my_flask_app')

users = [
    {'id': 1, 'name': 'John Doe le papy', 'email': 'papy@doe.me'},
    {'id': 2, 'name': 'John Doe le daron', 'email': 'daron@doe.me'},
    {'id': 3, 'name': 'John Doe le jeune', 'email': 'jeune@doe.me'},
    {'id': 4, 'name': 'Jane Doe la mamie', 'email': 'mamie@doe.me'},
    {'id': 5, 'name': 'Jane Doe la daronne', 'email': 'daronne@doe.me'}
]


@app.route('/create_user', methods=['POST'])
@app.route('/create_user/', methods=['POST'])
def create_user():
    data = request.get_json()
    if data is None:
        return jsonify({'message': 'Cannot create a user: no data'}), 404
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(user)
    return jsonify(users), 201


@app.route('/', methods=['GET'])
@app.route('/users', methods=['GET'])
@app.route('/users/', methods=['GET'])
@app.route('/user', methods=['GET'])
@app.route('/user/', methods=['GET'])
def get_users():
    return jsonify(users)


@app.route('/user/<int:user_id>', methods=['GET'])
@app.route('/user/<int:user_id>/', methods=['GET'])
def get_user(user_id: int):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user)


@app.route('/update_user/<int:user_id>', methods=['PUT'])
@app.route('/update_user/<int:user_id>/', methods=['PUT'])
def update_user(user_id: int):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            data = request.get_json()
            if data is None:
                return jsonify({'message': 'Cannot update a user: no data'}), 404
            user['name'] = data['name']
            user['email'] = data['email']
            users.pop(i)
            users.insert(i, user)
            return jsonify(users)


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
@app.route('/delete_user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id: int):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify(users)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
