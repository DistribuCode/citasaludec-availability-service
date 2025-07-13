from fastapi import HTTPException
from src.models.availability_model import Availability
from src.services import availability_service

async def create(data: Availability):
    id = await availability_service.create_availability(data)
    return {"message": "Availability created", "id": id}

async def list_all():
    return await availability_service.get_availabilities()

async def get_by_user(user_id: str):
    result = await availability_service.get_availability_by_user(user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Availability not found")
    return result

async def delete(user_id: str):
    result = await availability_service.delete_availability(user_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Deleted"}
