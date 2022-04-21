from pydantic import BaseModel


class Schema(BaseModel):
    class Config:
        orm_mode = True
