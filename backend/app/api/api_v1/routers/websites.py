from fastapi import APIRouter, Depends

from app import schemas
from app.crud.website import get_website
from app.db.session import get_db

websites_router = r = APIRouter()


@r.get("/get_website_bias", response_model=schemas.Bias)
async def get_website_bias(website_url: str, db=Depends(get_db)):
    """Get a website's bias."""
    website = get_website(db, website_url)
    return schemas.Bias(coefficient=website.avg_bias)
