from src.database.database import db
from src.models.availability_model import Availability

collection = db["availabilities"]

def fix_id(doc):
    doc["_id"] = str(doc["_id"])
    return doc

async def create_availability(data: Availability):
    result = await collection.insert_one(data.dict())
    return str(result.inserted_id)

async def get_availabilities():
    cursor = collection.find()
    return [fix_id(doc) async for doc in cursor]

async def get_availability_by_user(user_id: str):
    doc = await collection.find_one({"user_id": user_id})
    if doc:
        return fix_id(doc)
    return None

async def delete_availability(user_id: str):
    return await collection.delete_one({"user_id": user_id})
