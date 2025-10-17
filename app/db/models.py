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


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    hmac_id = Column(Integer, ForeignKey('hmac_keys.id'))
    encrypted_name = Column(String, nullable=False)
    encrypted_email = Column(String, nullable=False)
    encrypted_dob = Column(String)

    hmac = relationship('HMACTable', back_populates='user')
