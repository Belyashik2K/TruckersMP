from pydantic import BaseModel
from typing import Optional

class News(BaseModel):
    """Represents a news article from TruckersMP's API."""
    id: int
    title: str
    content_summary: str
    content: Optional[str] # This is optional because if you get all news articles, it won't return the content.
    author_id: int
    author: str
    pinned: bool
    updated_at: str
    published_at: str