"""This module contains the models for the API."""

from __future__ import annotations

from pydantic import BaseModel


class UserBase(BaseModel):
  """User base model."""
  name: str
  email: str

class UserCreate(UserBase):
  """User create model."""

class User(BaseModel):
  """User model."""
  id: int
  class Config:
    orm_mode = True

class PortfolioBase(BaseModel):
  """Portfolio model."""
  name: str
  user_id: int

class PortfolioCreate(PortfolioBase):
  """Portfolio create model."""

class Portfolio(PortfolioBase):
  """Portfolio model."""
  id: int
  user: User
  class Config:
    orm_mode = True


class Position(BaseModel):
  """Position model."""
  exchange: str
  symbol: str
  quantity: int
  price: float
  date: str