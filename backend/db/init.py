import json
import sys
from distutils.command.config import LANG_EXT

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

"""
予めデータベースは作成しておく必要があります。
CREATE DATABASE mydatabase;
"""

sys.path.append("..")

from settings import settings

Base = declarative_base()  # type: ignore


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


engine = create_engine(settings.MYSQL_URL)
Base.metadata.create_all(engine)

json_file_path = "../scripts/scraping/data/engineering/工学部Sセメスター_refined.json"

with open(json_file_path, "r") as f:
    class_data_list = json.load(f)

with Session(engine) as session:
    for class_data in class_data_list:
        # `plan` データの長さが特定の値より大きい場合に切り詰める
        if len(class_data["plan"]) > 65535:
            class_data["plan"] = class_data["plan"][:65535]

        class_instance = ClassModel(
            name=class_data["name"],
            credits=class_data["credits"],
            semester=", ".join(class_data["semester"]),
            day=", ".join(class_data["day"]),
            period=", ".join(class_data["period"]),
            plan=class_data["plan"],
            how_grading=class_data["how_grading"],
            caution=class_data["caution"],
            department=class_data["department"],
            teacher=class_data["teacher"],
        )
        session.add(class_instance)
    session.commit()


print("データがデータベースに保存されました。")
