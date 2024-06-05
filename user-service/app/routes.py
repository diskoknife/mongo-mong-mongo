from flask import Blueprint, jsonify, request
# import every created model
from .models import (
    get_user,
    create_user,
    update_user,
    delete_user
)
from .schemas import UserCreateSchema, UserUpdateSchema
from pydantic import ValidationError




main_bp = Blueprint('main', __name__)

@main_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    try:
        user = UserCreateSchema(**user_data)  # Validate input data
    except ValidationError as e:
        return jsonify(e.errors()), 400 

# GET all users
@main_bp.route('/users', methods=['GET'])
def get_users():
    users = list(user_collection.find())
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify(users)

# GET user by ID
@main_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user["_id"] = str(user["_id"])
    return jsonify(user)

# POST (create) a new user
@main_bp.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    # Add validation here (e.g., using Pydantic)
    
    new_user = create_user(user_data)
    new_user["_id"] = str(new_user["_id"])
    return jsonify(new_user), 201

# PUT (update) a user by ID
@main_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    update_data = request.get_json()
    # Add validation here (e.g., using Pydantic)

    updated_user = update_user(user_id, update_data)
    updated_user["_id"] = str(updated_user["_id"])
    return jsonify(updated_user)

# DELETE a user by ID
@main_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = get_user(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    delete_user(user_id)
    return '', 204
