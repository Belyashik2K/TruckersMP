from pydantic import BaseModel
from typing import Optional

class Socials(BaseModel):
    """Represents a VTC's socials from TruckersMP's API.
    
    This is optional because VTC is not required to have socials."""
    twitter: Optional[str]
    facebook: Optional[str]
    twitch: Optional[str]
    discord: Optional[str]
    youtube: Optional[str]

class Games(BaseModel):
    """Represents a VTC's games from TruckersMP's API."""
    ats: bool
    ets: bool

class VTC(BaseModel):
    """Represents a VTC from TruckersMP's API."""
    id: int
    name: str
    owner_id: int
    owner_username: str
    slogan: str
    tag: str
    website: Optional[str] # This is optional because VTC is not required to have website.
    socials: Socials
    games: Games
    members_count: int
    recruitment: str
    language: str
    verified: bool
    validated: bool
    created: str

class VTCTypes(BaseModel):
    """Represents a VTC type from TruckersMP's API."""
    recent: list[VTC]
    featured: list[VTC]
    featured_cover: list[VTC]
