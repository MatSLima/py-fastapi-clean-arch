from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship

from app.infra.sql_app.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="users")
    claims = relationship("UserClaim", back_populates="user")


class UserClaim(Base):
    __tablename__ = "user_claims"

    user_id = Column(Integer, ForeignKey("users.id"))
    claim_id = Column(Integer, ForeignKey("claims.id"))

    user = relationship("User", back_populates="claims")
    claim = relationship("Claim", back_populates="claims")

    __table_args__ = (
        PrimaryKeyConstraint(user_id, claim_id),
    )


class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    active = Column(Boolean, default=True)

    claims = relationship("UserClaim", back_populates="claim")


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

    users = relationship("User", back_populates="role")
