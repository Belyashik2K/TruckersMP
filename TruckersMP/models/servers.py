from pydantic import BaseModel
from typing import Optional 

class Server(BaseModel):
    """Represents a server from TruckersMP's API."""
    id: int
    game: str
    ip: str
    port: int
    name: str
    shortname: str
    idprefix: Optional[str] # This is optional, but I don't know what is this xD
    online: bool
    players: int
    queue: int
    maxplayers: int
    mapid: int
    displayorder: int
    speedlimiter: int
    collisions: bool
    carsforplayers: bool
    policecarsforplayers: bool
    afkenabled: bool
    event: bool
    specialEvent: bool
    promods: bool
    syncdelay: int
