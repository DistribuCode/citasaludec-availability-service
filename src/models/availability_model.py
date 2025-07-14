from pydantic import BaseModel
from typing import Optional

class Availability(BaseModel):
    user_id: str
    available: bool
    notes: Optional[str] = None
