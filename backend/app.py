"""

"""

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import Column, Integer, String, Text, create_engine, select
from sqlalchemy.orm import Session

from db.models import ClassModel
from settings import settings

engine = create_engine(settings.MYSQL_URL)

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ReactアプリケーションのURLに合わせて設定
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)


# データベースセッションを生成する依存関係
def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/search")
def search(
    department: str = "航空宇宙工学科",
    day: str = "火",
    period: str = "2",
    semester: str = "S1",
    db: Session = Depends(get_db),
):
    print(department, day, period, semester)
    """指定された条件に基づいて授業情報を検索するエンドポイント"""
    try:
        query = db.query(ClassModel).filter(
            ClassModel.department == department,
            ClassModel.day.contains(day),
            ClassModel.period.contains(period),
            ClassModel.semester.contains(semester),
        )
        result = query.all()
        if not result:
            raise HTTPException(
                status_code=404, detail="該当する授業は見つかりませんでした。"
            )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
