from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app import models


def add_website(db: Session, website_url: str, bias: Optional[float] = None) -> models.Website:
    if db.query(models.Website).filter(models.Website.url == website_url).first():
        raise HTTPException(status_code=400, detail="Website already exists")
    split_url = website_url.split("://")[1].split("/")[0].split(".")
    if len(split_url) > 2:
        name = split_url[1].capitalize()
    else:
        name = split_url[0].capitalize()
    if bias:
        website = models.Website(url=website_url, name=name, avg_bias=bias, num_data_points=1)
    else:
        website = models.Website(url=website_url, name=name)
    db.add(website)
    db.commit()
    db.refresh(website)
    return website


def get_website(
    db: Session,
    website_url: str,
) -> models.Website:
    website = db.query(models.Website).filter(models.Website.url == website_url).first()
    if not website:
        raise HTTPException(status_code=404, detail="Website not found")
    return website


def update_website(db: Session, website_url: str, new_bias: float) -> models.Website:
    website_url = website_url.replace("www.", "")
    website = db.query(models.Website).filter(models.Website.url == website_url).first()
    if not website:
        website = add_website(db, website_url, new_bias)
    else:
        num_data_points = website.num_data_points
        new_avg = (float(website.avg_bias) * float(num_data_points) + new_bias) / (num_data_points + 1)
        website.avg_bias = round(float(new_avg), 5)
        website.num_data_points = num_data_points + 1
        db.add(website)
        db.commit()
        db.refresh(website)
    return website
