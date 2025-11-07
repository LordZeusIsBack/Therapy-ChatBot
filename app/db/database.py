import os

import dotenv
from pgvector.psycopg2 import register_vector
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base


dotenv.load_dotenv()
DB_URL = os.getenv('DATABASE_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)

@event.listens_for(engine, 'connect')
def connect(db_api_connection, connection_record):
    register_vector(db_api_connection)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
