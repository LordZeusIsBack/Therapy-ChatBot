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
    """
    Enable pgvector support on a newly established DB-API connection.
    
    Parameters:
        db_api_connection: The raw DB-API connection object provided by the SQLAlchemy engine; pgvector types are registered on this connection.
        connection_record: The SQLAlchemy connection record for the new connection (unused by this function).
    """
    register_vector(db_api_connection)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()