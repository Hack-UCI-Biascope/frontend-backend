#!/usr/bin/env python3

from app.crud.user import create_user
from app.db.session import SessionLocal
from app.schemas.user import UserCreate


def init() -> None:
    db = SessionLocal()

    create_user(
        db,
        UserCreate(
            email="raviriley@gmail.com",
            password="186d580cbf9b546467925b12af9e730e09ccca8078bcd189c5ab338e8c3787dc",
            is_active=True,
            is_superuser=True,
        ),
    )


if __name__ == "__main__":
    print("Creating superuser raviriley@gmail.com")
    init()
    print("Superuser created")
