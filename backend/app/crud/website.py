from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import models


def get_website(
    db: Session,
    website_url: str,
) -> models.Website:
    website = db.query(models.Website).filter(models.Website.url == website_url).first()
    if not website:
        raise HTTPException(status_code=404, detail="Website not found")
    return website


def update_website(db: Session, website_url: str, new_bias: float) -> models.Website:
    website = get_website(db, website_url)
    num_data_points = website.num_data_points
    new_avg = (website.avg_bias * num_data_points + new_bias) / (num_data_points + 1)
    website.avg_bias = new_avg
    website.num_data_points = num_data_points + 1
    db.add(website)
    db.commit()
    db.refresh(website)
    return website
