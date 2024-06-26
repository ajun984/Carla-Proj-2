from dataclasses import dataclass
from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

@dataclass
class WorkId(Base):
    __tablename__ = "work_id"

    __id: int = Column(Integer, primary_key=True, autoincrement=True, name="id")

    def get_id(self):
        return self.__id
