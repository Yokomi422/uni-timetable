import json
import re
import unicodedata

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel


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


engineering_json_path = "./工学部Sセメスター.json"

with open(engineering_json_path, "r") as f:
    json_classes: list[dict] = json.load(f)

classes: list[ClassAttributesScraping] = [
    ClassAttributesScraping(**c) for c in json_classes
]


def map_code_department(code: str) -> str:
    mapping = {
        "AA": "航空宇宙工学科",
        "CE": "社会基盤学科",
        "AR": "建築学科",
        "UE": "都市工学科",
        "ME": "機械工学科",
        "MI": "機械情報工学科",
        "EE": "電子情報系",
        "AM": "応用物理系",
        "AP": "物理工学科",
        "MP": "計数工学科",
        "MA": "マテリアル工学科",
        "CH": "化学・生命系",
        "CA": "応用化学科",
        "CS": "化学システム工学科",
        "CB": "化学生命工学科",
        "SI": "システム創成学科",
        "SA": "環境・エネルギーシステムコース",
        "SB": "システムデザイン＆マネジメントコース",
        "SC": "知能社会システムコース",
    }

    if code in mapping:
        return mapping[code]
    else:
        return "その他"


def data_processing(c: ClassAttributesScraping) -> ClassAttributes:
    # 学科情報の取得
    code = c.code.split("\n")[0]
    pattern = r"[A-Z]{3}-([A-Z]{2})"
    match = re.search(pattern, code)
    department = map_code_department(match.group(1))
    # 曜限情報の取得
    periods = re.split(r"[ 、]", c.period)
    day = []
    _period = []
    for period in periods:
        if not "曜" in period:
            day.append("その他")
            _period.append("その他")
        else:
            day.append(period[0:2])
            _period.append(period[2:])

    # dayの重複を削除
    day = list(set(day))

    refined_data = ClassAttributes(
        name=c.name,
        teacher=unicodedata.normalize("NFKC", c.teacher),
        semester=c.semester.split(" "),
        department=department,
        credits=c.credits,
        day=day,
        period=_period,
        plan=c.plan,
        how_grading=c.how_grading,
        caution=c.caution,
    )

    return refined_data


refined_infos = []

for c in classes:
    if c.name == "None":
        continue

    refined_info = data_processing(c)
    refined_infos.append(refined_info)

# Pydanticモデルを辞書形式に変換
refined_dicts = [jsonable_encoder(c) for c in refined_infos]

refined_json_path = "./工学部Sセメスター_refined.json"
with open(refined_json_path, "w") as f:
    json.dump(refined_dicts, f, ensure_ascii=False, indent=2)
