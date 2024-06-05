import logging
import jwt
from flask import jsonify, make_response

from app.utils import get_jwt_identity

logger = logging.getLogger(__name__)


def register_error_handlers(app):
    """Registers error handlers for the Flask application."""

    @app.errorhandler(400)
    def bad_request(error):
        logger.error(f"Bad Request: {error}")
        return make_response(jsonify({"error": str(error)}), 400)

    @app.errorhandler(401)
    def unauthorized(error):
        logger.error(f"Unauthorized: {error}")
        return make_response(jsonify({"error": "Unauthorized"}), 401)

    @app.errorhandler(403)
    def forbidden(error):
        logger.error(f"Forbidden: {error}")
        return make_response(jsonify({"error": "Forbidden"}), 403)
    @app.errorhandler(404)
    def not_found(error):
        logger.error(f"Not Found: {error}")
        return make_response(jsonify({"error": "Not Found"}), 404)

    @app.errorhandler(409)
    def conflict(error):
        logger.error(f"Conflict: {error}")
        return make_response(jsonify({"error": "Conflict"}), 409)

    @app.errorhandler(422)
    def unprocessable_entity(error):
        logger.error(f"Unprocessable Entity: {error}")
        return make_response(jsonify({"error": "Unprocessable Entity"}), 422)

    @app.errorhandler(500)
    def internal_server_error(error):
        logger.error(f"Internal Server Error: {error}")
        return make_response(jsonify({"error": "Internal Server Error"}), 500)

    @app.errorhandler(jwt.ExpiredSignatureError)
    def expired_token(error):
        logger.error(f"Expired Token: {error}")
        return make_response(jsonify({"error": "Token has expired"}), 401)

    @app.errorhandler(jwt.InvalidTokenError)
    def invalid_token(error):
        logger.error(f"Invalid Token: {error}")
        return make_response(jsonify({"error": "Invalid token"}), 401)

    @app.errorhandler(jwt.DecodeError)
    def decode_token(error):
        logger.error(f"Decode Token: {error}")
        return make_response(jsonify({"error": "Decode token"}), 401)

    @app.errorhandler(jwt.InvalidSignatureError)
    def invalid_signature(error):
        logger.error(f"Invalid Signature: {error}")
        return make_response(jsonify({"error": "Invalid signature"}), 401)