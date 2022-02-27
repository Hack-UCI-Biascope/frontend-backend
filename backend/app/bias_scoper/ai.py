import random
from typing import List


class BiasScoper:
    def __init__(self, paragraphs: List[str]):
        self.paragraphs: List[str] = paragraphs
        self.article: str = "\n".join(paragraphs)
        self.bias: int = -1

    def get_paragraph_bias(self, paragraph: str) -> float:
        """Get the bias of a paragraph in an article."""
        # return a random float between -1 and 1
        return round(random.uniform(0, 1), 2)

    def get_article_bias(self) -> float:
        """Get the bias of an article."""
        return round(random.uniform(0, 1), 2)
