#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""API for the pman package."""
from __future__ import annotations

import fastapi
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from pman import database as models

ENGINE = create_engine("sqlite:///pman.db")

APP = fastapi.FastAPI()

@APP.get("/")
async def read_root() -> dict[str, str]:
  """Root endpoint for the API.

  Returns:
      dict[str, str]: Returns a dictionary with a single key-value pair.
  """
  return {"Hello": "World"}

@APP.post("/user", status_code=201)
def create_user(user: dict[str, str]) -> dict[str, str]:
  """Create a user.

  Args:
      user (dict[str, str]): The user to create.

  Returns:
      dict[str, str]: The user that was created.
  """
  with Session(ENGINE) as session:
    user_add = models.User(name=user["name"], email=user["email"])
    session.add(user_add)
    session.commit()
  return user

@APP.post("/position")
async def add_position(position: dict[str, float]) -> dict[str, float]:
  """Add a trade to the database.

  Args:
      position (dict[str, float]): The position to add to the database.

  Returns:
      dict[str, float]: The position that was added to the database.
  """
  return position

@APP.get("/position")
async def get_positions() -> list[dict[str, float]]:
  """Get all positions from the database.

  Returns:
      list[dict[str, float]]: A list of all positions in the database.
  """
  

@APP.delete("/position")
async def delete_positions() -> dict[str, str]:
  """Delete positions from the database.

  Returns:
      dict[str, str]: A dictionary with a single key-value pair.
  """
  return {"message": "All positions have been deleted."}

if __name__ == "__main__":
  uvicorn.run(APP, host="127.0.0.1", port=8000)