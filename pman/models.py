"""SQLAlchemy models for the pman package."""

from __future__ import annotations

from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import (
  Mapped,
  mapped_column,
  relationship,
  sessionmaker,
)

from .database import Base

POSITION_ID_FOREIGN_KEY = "position.id"

class User(Base):
  """User model."""
  __tablename__ = "user_account"
  
  id: Mapped[int] = mapped_column("id", primary_key=True)
  email: Mapped[str] = mapped_column("email")


class Portfolio(Base):
  """Portfolio model."""
  __tablename__ = "portfolio"
  
  id: Mapped[int] = mapped_column("id", primary_key=True)
  name: Mapped[str] = mapped_column("name")
  user_id: Mapped[int] = mapped_column("user_id", ForeignKey("user_account.id"))
  user: Mapped[User] = relationship("User", backref="portfolios")


class Position(Base):
  """Position model."""
  __tablename__ = "position"
  
  id: Mapped[int] = mapped_column("id", primary_key=True)
  portfolio_id: Mapped[int] = mapped_column(
      "portfolio_id", ForeignKey("portfolio.id"))
  portfolio: Mapped[Portfolio] = relationship("Portfolio", backref="positions")
  exchange: Mapped[str] = mapped_column("exchange")
  symbol: Mapped[str] = mapped_column("symbol")
  quantity: Mapped[int] = mapped_column("quantity")
  price: Mapped[float] = mapped_column("price")
  date: Mapped[str] = mapped_column("date")

def generate_schema() -> None:
  """Generate the database schema."""
  engine = create_engine("sqlite:///pman.db")
  Base.metadata.create_all(engine)

  session_handler = sessionmaker(bind=engine)
  session = session_handler()
  session.commit()
  session.close()