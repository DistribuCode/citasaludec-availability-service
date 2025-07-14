from fastapi import APIRouter, Depends
from src.controllers import availability_controller
from src.models.availability_model import Availability
from src.utils.auth import verify_token

router = APIRouter()

@router.post("/", dependencies=[Depends(verify_token)])
async def create(data: Availability):
    return await availability_controller.create(data)

@router.get("/", dependencies=[Depends(verify_token)])
async def list_all():
    return await availability_controller.list_all()

@router.get("/{user_id}", dependencies=[Depends(verify_token)])
async def get_by_user(user_id: str):
    return await availability_controller.get_by_user(user_id)

@router.delete("/{user_id}", dependencies=[Depends(verify_token)])
async def delete(user_id: str):
    return await availability_controller.delete(user_id)
