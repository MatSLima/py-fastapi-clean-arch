import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, PrimaryKeyConstraint, DateTime
from sqlalchemy.orm import relationship

from app.infra.sql_app.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    role = relationship("RoleModel", back_populates="users")
    claims = relationship("UserClaimModel", back_populates="user")


class UserClaimModel(Base):
    __tablename__ = "user_claims"

    user_id = Column(Integer, ForeignKey("users.id"))
    claim_id = Column(Integer, ForeignKey("claims.id"))

    user = relationship("UserModel", back_populates="claims")
    claim = relationship("ClaimModel", back_populates="claims")

    __table_args__ = (
        PrimaryKeyConstraint(user_id, claim_id),
    )


class ClaimModel(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    active = Column(Boolean, default=True)

    claims = relationship("UserClaimModel", back_populates="claim")


class RoleModel(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

    users = relationship("UserModel", back_populates="role")
