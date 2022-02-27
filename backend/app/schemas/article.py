from typing import List, Optional

from pydantic import BaseModel


class ArticleData(BaseModel):
    website_url: str
    paragraphs: List[str]
    chosen_paragraph: Optional[str] = None
