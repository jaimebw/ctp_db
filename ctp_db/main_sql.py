# author: Jaime Bowen

from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine, select
import pandas as pd
from .table_structure import *

test_data = {"nct_id": "NCT01017328", "brief_summary": "lol"}
engine = create_engine("sqlite:///test_database.db")

SQLModel.metadata.create_all(engine)

test_entry = CTPEntry(
    nct_id=test_data["nct_id"], brief_summary=test_data["brief_summary"]
)
with Session(engine) as session:
    session.add(test_entry)
    session.commit()

with Session(engine) as session:
    statement = select(CTPEntry).where(CTPEntry.nct_id == "NCT01017328")
    hero = session.exec(statement).first()
    print(hero)
