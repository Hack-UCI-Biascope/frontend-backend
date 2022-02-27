import random
from typing import List

from app import schemas


class BiasScoper:
    # loaded_model = pickle.load(open("nb.pkl", "rb"))

    def __init__(self, paragraphs: List[str]):
        self.paragraphs: List[str] = paragraphs
        self.article: str = "\n".join(paragraphs)
        self.bias: float = -1.0

    def get_article_bias(self) -> schemas.ArticleBias:
        """Get the bias of an article."""
        # self.bias = self.loaded_model.predict([self.article])
        self.bias = round(random.uniform(0, 1), 2)
        paragraph_biases = [self.get_paragraph_bias(paragraph) for paragraph in self.paragraphs]
        return schemas.ArticleBias(coefficient=self.bias, paragraph_biases=paragraph_biases)

    def get_paragraph_bias(self, paragraph: str) -> float:
        """Get the bias of a paragraph in an article."""
        # bias = self.loaded_model.predict([paragraph])
        # conversion = {"Left": -1, "Lean Left": -0.5, "Center": 0, "Lean Right": 0.5, "Right": 1}
        # return conversion[bias[0]]
        return round(random.uniform(0, 1), 2)
