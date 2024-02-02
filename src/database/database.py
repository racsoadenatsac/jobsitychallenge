from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Configuration
DATABASE_URI = 'postgresql://username:password@localhost:5432/mydatabase'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def get_session():
    return Session()

# You can include this to create tables if they don't exist
if __name__ == '__main__':
    create_tables()

