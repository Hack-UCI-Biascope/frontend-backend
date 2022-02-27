#!/usr/bin/env python3
from app import models
from app.crud.user import create_user
from app.db.session import SessionLocal
from app.schemas.user import UserCreate


def init() -> None:
    db = SessionLocal()

    db.query(models.User).delete()
    db.commit()

    user_to_create = UserCreate(
        email="raviriley@gmail.com",
        password="186d580cbf9b546467925b12af9e730e09ccca8078bcd189c5ab338e8c3787dc",
        is_active=True,
        is_superuser=True,
    )

    if db.query(models.User).filter(models.User.email == user_to_create.email).first() is None:
        create_user(
            db,
            user_to_create,
        )


if __name__ == "__main__":
    print("Creating superuser raviriley@gmail.com")
    init()
    print("Superuser created")
