from fastapi import APIRouter, Depends, HTTPException

from app import schemas
from app.bias_scoper.ai import BiasScoper
from app.crud.website import update_website
from app.db.session import get_db

articles_router = r = APIRouter()


@r.post("/article_bias", response_model=schemas.ArticleBias)
async def compute_article_bias(article_data: schemas.ArticleData, db=Depends(get_db)):
    """Compute an article's bias."""
    # get the bias of the article
    paragraphs = article_data.paragraphs
    article_bias = BiasScoper(paragraphs).get_article_bias()
    # update the average bias of the website the article came from
    update_website(db, article_data.website_url, article_bias.coefficient)
    return article_bias


@r.post("/paragraph_bias", response_model=schemas.Bias)
async def compute_paragraph_bias(article_data: schemas.ArticleData):
    """Compute a paragraph's bias of an article."""
    chosen_paragraph = article_data.chosen_paragraph
    if not chosen_paragraph:
        raise HTTPException(status_code=400, detail="No paragraph chosen.")
    # get the bias of the paragraph
    paragraphs = article_data.paragraphs
    bias = BiasScoper(paragraphs).get_paragraph_bias(chosen_paragraph)
    return schemas.Bias(coefficient=bias)
