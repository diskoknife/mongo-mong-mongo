import redis
from app.config import settings

# Establish a connection to your Redis server
redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


# Create pub event for creating user
def publish_user_created(user_id):
    """Publishes a message to the Redis pub/sub channel when a new user is created."""
    redis_client.publish(settings.REDIS_USER_CREATED_CHANNEL, user_id)
