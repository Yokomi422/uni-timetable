from sqlalchemy import Column, Integer, String, Text, create_engine, select
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()


class ClassModel(Base):  # type: ignore
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    credits = Column(Integer)
    semester = Column(String(255))
    teacher = Column(String(100))
    department = Column(String(100))
    day = Column(String(50))
    period = Column(String(50))
    plan = Column(LONGTEXT)
    how_grading = Column(Text)
    caution = Column(LONGTEXT)
