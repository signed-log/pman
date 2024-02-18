
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
  DeclarativeBase,
  Mapped,
  MappedAsDataclass,
  mapped_column,
  relationship,
)

POSITION_ID_FOREIGN_KEY = "position.id"


class Base(MappedAsDataclass, DeclarativeBase):
  """Base SQLAlchemy model class."""

class Transaction(Base):
  """Transaction model."""
  __tablename__ = "transaction"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="transactions")
  date: Mapped[str] = mapped_column("date")
  quantity: Mapped[int] = mapped_column("quantity")
  price: Mapped[float] = mapped_column("price")
  type: Mapped[str] = mapped_column("type")
  commission: Mapped[float] = mapped_column("commission")
  fees: Mapped[float] = mapped_column("fees")
  notes: Mapped[str] = mapped_column("notes")


class Dividend(Base):
  """Dividend model."""
  __tablename__ = "dividend"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey("position.id"))
  position: Mapped[Position] = relationship("Position", backref="dividends")
  date: Mapped[str] = mapped_column("date")
  amount: Mapped[float] = mapped_column("amount")
  notes: Mapped[str] = mapped_column("notes")


class Interest(Base):
  """Interest model."""
  __tablename__ = "interest"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="interests")
  date: Mapped[str] = mapped_column("date")
  amount: Mapped[float] = mapped_column("amount")
  notes: Mapped[str] = mapped_column("notes")


class Fee(Base):
  """Fee model."""
  __tablename__ = "fee"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="fees")
  date: Mapped[str] = mapped_column("date")
  amount: Mapped[float] = mapped_column("amount")
  notes: Mapped[str] = mapped_column("notes")


class Tax(Base):
  """Tax model."""
  __tablename__ = "tax"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="taxes")
  date: Mapped[str] = mapped_column("date")
  amount: Mapped[float] = mapped_column("amount")
  notes: Mapped[str] = mapped_column("notes")


class StockSplit(Base):
  """Stock split model."""
  __tablename__ = "stock_split"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="stock_splits")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockMerge(Base):
  """Stock merge model."""
  __tablename__ = "stock_merge"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="stock_merges")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockSpinoff(Base):
  """Stock spinoff model."""
  __tablename__ = "stock_spinoff"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_spinoffs")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockDividend(Base):
  """Stock dividend model."""
  __tablename__ = "stock_dividend"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_dividends")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockBonus(Base):
  """Stock bonus model."""
  __tablename__ = "stock_bonus"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_bonuses")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockRights(Base):
  """Stock rights model."""
  __tablename__ = "stock_rights"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="stock_rights")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockBuyback(Base):
  """Stock buyback model."""
  __tablename__ = "stock_buyback"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_buybacks")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockConversion(Base):
  """Stock conversion model."""
  __tablename__ = "stock_conversion"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_conversions")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockReclassification(Base):
  """Stock reclassification model."""
  __tablename__ = "stock_reclassification"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_reclassifications")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockReorganization(Base):
  """Stock reorganization model."""
  __tablename__ = "stock_reorganization"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_reorganizations")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockLiquidation(Base):
  """Stock liquidation model."""
  __tablename__ = "stock_liquidation"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship(
      "Position", backref="stock_liquidations")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockOther(Base):
  """Stock other model."""
  __tablename__ = "stock_other"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="stock_others")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class StockEvent(Base):
  """Stock event model."""
  __tablename__ = "stock_event"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="stock_events")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class Stock(Base):
  """Stock model."""
  __tablename__ = "stock"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="stocks")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")


class Bond(Base):
  """Bond model."""
  __tablename__ = "bond"

  id: Mapped[int] = mapped_column("id", primary_key=True)
  position_id: Mapped[int] = mapped_column(
      "position_id", ForeignKey(POSITION_ID_FOREIGN_KEY))
  position: Mapped[Position] = relationship("Position", backref="bonds")
  date: Mapped[str] = mapped_column("date")
  ratio: Mapped[float] = mapped_column("ratio")
  notes: Mapped[str] = mapped_column("notes")
