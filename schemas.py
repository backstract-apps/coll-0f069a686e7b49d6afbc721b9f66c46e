from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Students(BaseModel):
    id: int
    created_at: datetime.time


class ReadStudents(BaseModel):
    id: int
    created_at: datetime.time
    class Config:
        from_attributes = True




class PostStudents(BaseModel):
    id: int
    created_at: Any

    class Config:
        from_attributes = True

