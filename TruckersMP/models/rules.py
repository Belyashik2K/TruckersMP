from pydantic import BaseModel

class Rules(BaseModel):
    """Represents the rules from TruckersMP's API."""
    rules: str
    revision: int