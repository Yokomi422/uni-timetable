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


class Class(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    credits: int
    semester: str
    department_id: Optional[int] = Field(default=None, foreign_key="department.id")
    department: Optional[Department] = Relationship(back_populates="classes")
    teacher_id: Optional[int] = Field(default=None, foreign_key="teacher.id")
    teacher: Optional[Teacher] = Relationship(back_populates="classes")
