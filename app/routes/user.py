from flask import Blueprint, request, jsonify
from app.models.user import User, create_user, read_user, update_user, delete_user

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['POST'])
def create():
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']

        user = create_user(username, email, password)

        return jsonify({'message': 'User created successfully', 'user': user}), 201
    except Exception as e:
        return jsonify({'message': 'Error creating user', 'error': str(e)}), 400

@user_routes.route('/users/<username>', methods=['GET'])
def read(username):
    try:
        user = read_user(username)

        if user:
            return jsonify({'message': 'User found', 'user': user}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error reading user', 'error': str(e)}), 400

@user_routes.route('/users/<username>', methods=['PUT'])
def update(username):
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']

        user = update_user(username, email, password)

        if user:
            return jsonify({'message': 'User updated successfully', 'user': user}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error updating user', 'error': str(e)}), 400

@user_routes.route('/users/<username>', methods=['DELETE'])
def delete(username):
    try:
        user = delete_user(username)

        if user:
            return jsonify({'message': 'User deleted successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'Error deleting user', 'error': str(e)}), 400