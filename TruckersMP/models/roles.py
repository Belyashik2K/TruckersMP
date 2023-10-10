from pydantic import BaseModel

class Role(BaseModel):
    """Represents a VTC role from TruckersMP's API."""
    id: int
    name: str
    order: int
    owner: bool
    created_at: str
    updated_at: str