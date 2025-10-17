from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class HMACTable(Base):
    __tablename__ = 'hmac_keys'

    id = Column(Integer, primary_key=True, index=True)
    user_identifier_hash = Column(String, unique=True, index=True, nullable=False)
    salt = Column(String, nullable=False)
    hmac_key = Column(String, nullable=False)
    user = relationship('User', back_populates='hmac', uselist=False)
