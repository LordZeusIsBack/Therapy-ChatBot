import os

import dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


dotenv.load_dotenv()
DB_URL = os.getenv('DATABASE_URL')

engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
