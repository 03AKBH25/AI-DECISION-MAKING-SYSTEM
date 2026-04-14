import redis

#connect to redis
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def add_message(user_id: str, message: str):
    key = f"conversation:{user_id}"
    redis_client.rpush(key,message)
    redis_client.ltrim(key, -5, -1) # keep last 5 messages

def get_messages(user_id: str):
    key = f"conversation:{user_id}"
    return redis_client.lrange(key, 0, -1)