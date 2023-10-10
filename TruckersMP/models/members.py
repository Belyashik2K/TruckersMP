from pydantic import BaseModel

class Member(BaseModel):
    """Represents a VTC member from TruckersMP's API."""
    id: int
    user_id: int
    username: str
    steam_id: int
    role_id: int
    role: str
    is_owner: bool
    joinDate: str