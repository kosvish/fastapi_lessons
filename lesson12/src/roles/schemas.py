from pydantic import BaseModel, Json


class CreateRole(BaseModel):
    id: int
    name: str
    permissions: str
