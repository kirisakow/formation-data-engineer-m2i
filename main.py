from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary storage for users
users = [
    {'id': 1, 'name': 'John Doe le papy', 'email': 'XXXXXX@XXXXX'},
    {'id': 2, 'name': 'John Doe le daron', 'email': 'XXXXXX@XXXXX'},
    {'id': 3, 'name': 'John Doe le jeune', 'email': 'XXXXXX@XXXXX'},
    {'id': 4, 'name': 'Jane Doe la mamie', 'email': 'XXXXXX@XXXXX'},
    {'id': 5, 'name': 'Jane Doe la daronne', 'email': 'XXXXXX@XXXXX'}
]

# CREATE: Create a user
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = {
        'id': len(users) + 1,
        'name': data['name'],
        'email': data['email']
    }
    users.append(user)
    return jsonify(user), 201

# RETRIEVE: Get all users
@app.route('/', methods=['GET'])
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# RETRIEVE: Get a user by ID
@app.route('/user/:user_id', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# UPDATE: Update a user
@app.route('/user/:user_id', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        data = request.get_json()
        user['name'] = data['name']
        user['email'] = data['email']
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# DELETE: Delete a user
@app.route('/user/:user_id', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9001, debug=True)

