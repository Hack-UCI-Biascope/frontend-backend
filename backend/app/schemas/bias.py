from pydantic import BaseModel


class Bias(BaseModel):
    coefficient: float
