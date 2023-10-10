from pydantic import BaseModel
from typing import Optional

class Bans(BaseModel):
    """Represents a ban from TruckersMP's API."""
    expiration: str
    timeAdded: str
    active: bool
    reason: str
    adminName: str
    adminID: Optional[int] # This is optional because if you has been banned by the system/moderator, it won't return the admin ID.
