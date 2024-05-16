import sys
import os
from openai import OpenAI
import re
from langchain.document_loaders import PyMuPDFLoader
from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document
sys.path.append('..')

from settings import settings
from models import models

timetable_files: list[str] = os.listdir("../data/department_timetables/")

client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
def create_message(page_content: str, department: str):
    content = f"""
        ## System
        You are an assistant tasked with extracting course names and instructor names from the {department} schedule PDF. Based on the following examples, return a list of [(course name, instructor name)] pairs.

        ## Data
        {page_content}

        ## Instruction    
        - 下ののExamplesを参考に[(授業名, 教員名)]のリストを返してください。以上のDataには、PDFのテキストが含まれています。
        - 授業の名前と教員の名前を抽出してください。[(授業名, 教員名), (授業名, 教員名)]の形式で返してください。日本語でお願いします。
        - 大学院の授業は除き、学部の授業のみを対象とします。
        - must be a list of tuples that can be processed by Python
        - if there is no teacher on a course, please return None, not an empty string, not surrounded by quotes, just None
        - definitely no prefill
        -  ending with like (, )] style
        - with no indent
        

        ## Examples
            - [("材料力学１", "山田太郎"), ("材料力学２", "山田太郎")]
            - [("材料力学１", "山田太郎"), ("材料力学２", "山田太郎"), ("材料力学３", "山田太郎")]
            - [("材料力学１", "山田太郎"), ("材料力学２", "山田太郎"), ("材料力学３", "山田太郎"), ("材料力学４", "山田太郎")]
            - [("材料力学１", "山田太郎"), ("材料力学２", "山田太郎"), ("材料力学３", "山田太郎"), ("材料力学４", "山田太郎"), ("材料力学５", "山田太郎")]
    """
    
    return content

def get_timetable_info(filename: str) -> list[tuple[str, str]]:
    """
    時間割のpdfから、(授業名、教員名)のリストを取得する関数
    """
    pattern = r"(.*)\.pdf"
    department = re.match(pattern, filename).group(1)
    file_path = f"../data/department_timetables/{filename}"
    loader = PyMuPDFLoader(file_path)
    pages = loader.load_and_split()
    
    responses = []
    
    for page in pages:
        content = page.page_content
        message = create_message(content, department)
        prompt = [
            {
                "role": "system",
                "content": "You are an assistant tasked with extracting course names and instructor names from the schedule PDF. Based on the following examples, return a list of [(course name, instructor name)] pairs."
            },
            {
                "role": "user",
                "content": content
            }
        ]
                
        response =  client.chat.completions.create(
            model = "gpt-4",
            messages = prompt,
            max_tokens=1024,
            temperature=0.0
        )
        
        responses.append(response.choices[0].message.content)

    return responses
    

def fetch_from_tables():
    """
    時間割の表から、(授業名、教員名)をtupleで取得する関数
    args: 
    """
    
    document_name = "建築学科.pdf"
    
    response = get_timetable_info(document_name)
    
    return response
    
response = fetch_from_tables()

lis = []

for res in response:
    res = res.replace("\n", "")
    message = f"""
        ## input
        {res}

        ## 注意点
        - no prefill
        - with no indent
        - must only only be a list of tuples that can be processed by Python, ending with like (, )] style
        - pythonのlistに含まれない形式では出力しないでください。prefillはつけないでください. 最初から[で初めてpythonのリスト形式になっている必要があります。
        - listの要素のtupleも必ず()で囲んでください
        - no prefill, just the list of tuples
        
        ## instructions
        - inputはpythonのlist形式でなければならないが、list形式でないです。途中で終わっている要素は削除していいので、それをlist形式に変換してください。
        
        ## output
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )
    # pattern = r"([.*])"

    resp = response.choices[0].message.content
    
    # a = re.match(pattern, resp).group(1)
    
    li = eval(resp)
    lis.extend(li)

print(lis)

"""
[('建築構造解析第二', '伊山'), ('建築設備第一', '赤司'), ('建築音環境', '佐久間'), ('建築光環境･視環境', '小﨑'), ('建築設計理論第一', '千葉・安原・三谷'), ('建築材料科学', '丸山'), ('日本建築史', '海野'), ('数学２Ｆ', '渡辺'), ('建築計画第一', '松田'), ('荷重外力論第二', '糸井'), ('建築材料演習', '野口・丸山・吉岡'), ('建築生産マネジメント概論', '権藤'), ('建築法規', '淡野'), ('工学英語コミュニケー ション演習', 'Unknown'), ('建築設計理論第二', '千葉・安原・三谷'), ('建築材料計画', '丸山'), ('建築計画第二', '大月'), ('建築空気環境・水環境', '前'), ('建築情報学概論', '池田'), ('鉄骨構造', '山田・伊山'), ('建築構造解析第三', '糸井'), ('数学３', '出口'), ('統計解析', '下野'), ('建築設備第三', '小﨑'), ('建築設計理論第四', '安原・千葉・三谷'), ('建築耐震構造', '山田'), ('西洋建築史', '加藤'), ('建築計画第三', '松田'), ('建築環境デザイン論', '前'), ('建築構造演習', '糸井・山田・藤田・田尻'), ('数理手法III', '寒野'), ('減災構造工学', '山田・清家・伊山'), ('建築設備第二', '前'), ('建築設計理論第三', '三谷・千葉・安原'), ('鉄筋コンクリート構造', '田尻'), ('建築計画第四', '大月'), ('建築防火工学', '野口・吉岡'), ('建築情報基盤学', '伊山・加藤'), ('造形第六', '千葉･安原'), ('建築耐震構造', '山田'), ('建築設計製図第五', '千葉･安原･他建築全教員'), ('建築施工', '高瀬'), ('環境･設備演習', '佐久間･赤司･前･小﨑・谷口'), ('鉄筋コンクリート構造', '田尻'), ('造形第五', '加藤･海野'), ('建築設計製図第五', '千葉･安原･他建築全教員'), ('日本住宅建築史', '海野'), ('建築構法特論', '藤田'), ('近代都市建築史', '加藤'), ('職業指導', '岩脇'), ('建築基礎構造', '糸井'), ('アカデミック・ライティング', ''), ('職業指導', '岩脇'), ('アカデミック・プレゼンテーション', ''), ('卒業考査', ''), ('卒業考査', ''), ('建築構法特論', '藤田'), ('鉄骨構造演習', '伊山・山田'), ('建築設計製図第七', '千葉･安原･他建築全教員'), ('建築設計製図第七', '千葉･安原･他建築全教員'), ('鉄筋コンクリート構造演習', '田尻'), ('卒業論文', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業制作', ''), ('卒業制作', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業論文', ''), ('卒業制作', ''), ('卒業制作', ''), ('卒業制作', ''), ('卒業制作', ''), ('卒業制作', ''), ('卒業制作', '')]
"""