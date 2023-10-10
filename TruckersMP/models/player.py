from typing import List, Union, Optional

from pydantic import BaseModel

class Patreon(BaseModel):
    """Represents a player's Patreon information from TruckersMP's API."""
    isPatron: bool
    active: bool
    # This is optional because if you aren't a patron, it won't return the following information.
    color: Optional[str]
    tierId: Optional[int]
    currentPledge: Optional[int]
    lifetimePledge: Optional[int]
    nextPledge: Optional[int]
    hidden: Optional[Union[bool, None]]

class Permissions(BaseModel):
    """Represents a player's permissions from TruckersMP's API."""
    isStaff: bool
    isUpperStaff: bool
    isGameAdmin: bool
    showDetailedOnWebMaps: bool

class VTCHistory(BaseModel):
    """Represents a VTC history from TruckersMP's API."""
    id: int
    name: str
    verified: bool
    joinDate: str
    leftDate: str

class VTC(BaseModel):
    """Represents a player VTC from TruckersMP's API."""
    id: int
    name: str
    tag: str
    inVTC: bool
    memberID: int

class Player(BaseModel):
    """Represents a player from TruckersMP's API."""
    id: int
    name: str
    avatar: str
    smallAvatar: str
    joinDate: str
    steamID64: int
    steamID: str
    discordSnowflake: Optional[str] # This is optional because if you don't have Discord linked, it won't return the Discord snowflake.
    displayVTCHistory: bool
    groupName: str
    groupColor: str
    groupID: int
    banned: bool
    bannedUntil: Optional[str] # This is optional because if you haven't been banned, it won't return the ban expiration date.
    bansCount: Optional[int] # This is optional because if you haven't been banned, it won't return the ban count.
    displayBans: bool
    patreon: Patreon
    permissions: Permissions
    vtc: VTC
    vtcHistory: Optional[List[VTCHistory]] # This is optional because if you haven't joined any VTC, it won't return the VTC history.
