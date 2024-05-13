from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
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
