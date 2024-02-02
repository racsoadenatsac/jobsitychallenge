from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Trip(Base):
    __tablename__ = 'trips'

    id = Column(Integer, primary_key=True)
    region = Column(String)
    origin_coord = Column(String)  # In a real-world scenario, you might want to store these as two separate float columns for latitude and longitude
    destination_coord = Column(String)  # Same note as origin_coord
    datetime = Column(DateTime)
    datasource = Column(String)

    def __repr__(self):
        return f"<Trip(region='{self.region}', datetime='{self.datetime}', datasource='{self.datasource}')>"

