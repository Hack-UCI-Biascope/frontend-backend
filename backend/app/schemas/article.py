from typing import List

from pydantic import BaseModel


class ArticleData(BaseModel):
    website_url: str
    paragraphs: List[str]
