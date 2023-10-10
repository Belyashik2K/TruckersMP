from pydantic import BaseModel
from typing import Optional, Any

class EventType(BaseModel):
    """Represents an event type from TruckersMP's API."""
    key: str
    name: str

class Location(BaseModel):
    """Represents a departure or arrival location from TruckersMP's API."""
    location: str
    city: str

class Server(BaseModel):
    """Represents a server info from TruckersMP's API."""
    id: int
    name: str

class VTC(BaseModel):
    """
    Represents a VTC that created event from TruckersMP's API.
    
    This is optional because VTC is not required to create an event.
    """
    id: Optional[int] 
    name: Optional[str]

class User(BaseModel):
    """Represents a user that created event from TruckersMP's API."""
    id: int
    username: str

class Attendances(BaseModel):
    """Represents an attendance from TruckersMP's API."""
    confirmed: int
    unsure: int
    vtcs: int

class Event(BaseModel):
    """Represents an event from TruckersMP's API."""
    id: int
    event_type: EventType
    name: str
    slug: str
    game: str
    server: Server
    language: str
    departure: Location
    arrive: Location
    start_at: str
    banner: Optional[str]
    map: Optional[str]
    description: str
    rule: Optional[str]
    voice_link: Optional[str]
    external_link: Optional[str]
    featured: str
    vtc: Optional[VTC]
    user: User
    attendances: Attendances
    dlcs: Any
    url: str
    created_at: str
    updated_at: str

class EventTypes(BaseModel):
    """Represents a list of event types from TruckersMP's API."""
    featured: Optional[list[Event]]
    today: Optional[list[Event]]
    now: Optional[list[Event]]
    upcoming: Optional[list[Event]]