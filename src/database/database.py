from motor.motor_asyncio import AsyncIOMotorClient
from src.config.settings import settings

client = AsyncIOMotorClient(settings.MONGO_URI)
db = client.get_default_database()
