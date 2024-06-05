from flask import Flask# Import configuration
from app.config import settings


# Create Flask app
app = Flask(__name__)


# Import error handlers
from app.errors import register_error_handlers

# Register error handlers
register_error_handlers(app)

# Import routes
from app.routes import main_bp

# Register blueprints
app.register_blueprint(main_bp)

# Initialize database connection
from app.models import client

# Initialize Redis connection
from app.redis import redis_client

# Run the app
if __name__ == "__main__":
    app.run(host=settings.HOST, port=settings.PORT)



