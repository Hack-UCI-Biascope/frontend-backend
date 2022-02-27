from sqlalchemy import Column, Float, Integer, String

from app.db.session import Base


class Website(Base):
    __tablename__ = "website"

    url = Column(String, primary_key=True, index=True, unique=True)
    name = Column(String)
    avg_bias = Column(Float, default=0.5, nullable=False)
    num_data_points = Column(Integer, default=0, nullable=False)
