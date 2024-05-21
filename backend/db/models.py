"""
サンプルデータを準備するときは、
以下のコマンドを実行してください。
```
python fix_copied_str.py [ファイル名] | pbcopy
```
"""

from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Faculty(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    departments: List["Department"] = Relationship(back_populates="faculty")


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    faculty_id: Optional[int] = Field(default=None, foreign_key="faculty.id")
    faculty: Optional[Faculty] = Relationship(back_populates="departments")
    classes: List["Class"] = Relationship(back_populates="department")


class Teacher(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    classes: List["Class"] = Relationship(back_populates="teacher")


# ひとまずこれしか使わない
class Class(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    credits: int
    semester: List[str] = Field(sa_column_kwargs={"type_": "TEXT"})
    day: List[str] = Field(sa_column_kwargs={"type_": "TEXT"})
    period: List[str] = Field(sa_column_kwargs={"type_": "TEXT"})
    plan: str
    how_grading: str
    caution: str
    department: str
    teacher: str
