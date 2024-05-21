from pydantic import BaseModel


class Urls(BaseModel):
    engineering: str
    science: str


urls = Urls(
    engineering="https://catalog.he.u-tokyo.ac.jp/result?q=&type=ug&faculty_id=3&facet=%7B%22semester_codes%22%3A%5B%22S1%22%2C%22S2%22%5D%7D&page=",
    science="https://catalog.he.u-tokyo.ac.jp/result?q=&type=ug&faculty_id=5&facet=%7B%7D&page=",
)


# インスタンスはimportできないため
def get_urls():
    return urls


class ClassAttributesScraping(BaseModel):
    name: str
    teacher: str
    semester: str
    credits: str
    period: str
    plan: str
    how_grading: str
    caution: str
    code: str


class ClassAttributes(BaseModel):
    name: str
    credits: str
    semester: list[str]
    teacher: str
    department: str
    day: list[str]
    period: list[str]
    plan: str
    how_grading: str
    caution: str
