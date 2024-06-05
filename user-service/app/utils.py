import logging

import jwt
from flask import current_app
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from werkzeug.exceptions import BadRequest, Unauthorized

from app.models import get_user, create_user, update_user, delete_user
from app.schemas import UserCreateSchema, UserUpdateSchema

logger = logging.getLogger(__name__)


def register_user(user_data):
    """Registers a new user."""

    try:
        user_schema = UserCreateSchema()
        validated_data = user_schema.load(user_data)

        # Check if user already exists
        existing_user = get_user(email=validated_data["email"])
        if existing_user:
            raise BadRequest("User with that email already exists.")

        # Create new user
        new_user = create_user(validated_data)

        # Generate access and refresh tokens
        access_token = create_access_token(identity=new_user.id)
        refresh_token = create_refresh_token(identity=new_user.id)

        return {
            "user": new_user,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    except Exception as e:
        logger.exception("Error registering user: %s", e)
        raise e


def login_user(email, password):
    """Logs in a user."""

    try:
        user = get_user(email=email)
        if not user or not user.check_password(password):
            raise Unauthorized("Invalid credentials.")

        # Generate access and refresh tokens
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "user": user,
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

    except Exception as e:
        logger.exception("Error logging in user: %s", e)
        raise e


def refresh_token(refresh_token):
    """Refreshes an access token."""       
    try:
        identity = get_jwt_identity()
        user = get_user(id=identity)

        # Check if refresh token is valid
        try:
            jwt.decode(refresh_token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise Unauthorized("Refresh token has expired.")
        except jwt.InvalidTokenError:
            raise Unauthorized("Invalid refresh token.")

        # Generate new access token
        access_token = create_access_token(identity=user.id)

        return {"access_token": access_token}

    except Exception as e:
        logger.exception("Error refreshing token: %s", e)
        raise e


def get_current_user():
    """Gets the currently logged-in user."""

    try:
        user_id = get_jwt_identity()
        user = get_user(id=user_id)
        return user

    except Exception as e:
        logger.exception("Error getting current user: %s", e)
        raise e


def update_user_profile(user_id, updated_data):
    """Updates a user's profile."""

    try:
        user_schema = UserUpdateSchema()
        validated_data = user_schema.load(updated_data)

        # Update user in database
        updated_user = update_user(user_id, validated_data)

        return updated_user

    except Exception as e:
        logger.exception("Error updating user profile: %s", e)
        raise e


def delete_user_account(user_id):
    """Deletes a user's account."""

    try:
        delete_user(user_id)

        return {"message": "User account deleted successfully."}

    except Exception as e:
        logger.exception("Error deleting user account: %s", e)
        raise e
