from typing import List

from pydantic import BaseModel


class Bias(BaseModel):
    coefficient: float


class ArticleBias(Bias):
    """Bias for an article."""

    paragraph_biases: List[float]
