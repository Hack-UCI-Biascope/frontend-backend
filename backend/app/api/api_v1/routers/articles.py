from fastapi import APIRouter, Depends

from app import schemas
from app.bias_scoper.ai import BiasScoper
from app.crud.website import update_website
from app.db.session import get_db

articles_router = r = APIRouter()


@r.post("/article_bias", response_model=schemas.Bias)
async def compute_article_bias(article_data: schemas.ArticleData, db=Depends(get_db)):
    """Compute a website's bias."""
    # get the bias of the article
    paragraphs = article_data.paragraphs
    bias = BiasScoper(paragraphs).get_article_bias()
    # update the average bias of the website the article came from
    update_website(db, article_data.website_url, bias)
    return schemas.Bias(coefficient=bias)
