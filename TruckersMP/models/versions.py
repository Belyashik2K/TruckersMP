from pydantic import BaseModel

class Checksum(BaseModel):
    """Represents a checksum from TruckersMP's API."""
    dll: str
    adb: str

class Versions(BaseModel):
    """Represents the current game version from TruckersMP's API."""
    name: str
    numeric: str
    stage: str
    ets2mp_checksum: Checksum
    atsmp_checksum: Checksum
    time: str
    supported_game_version: str
    supported_ats_game_version: str