import json
import time

from data.engineering.type import ClassAttributesScraping, get_urls
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def fetch_class_attributes(driver: WebDriver) -> ClassAttributesScraping:
    try:
        name = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-table-cell.name-cell"
        )[1].text
    except (IndexError, NoSuchElementException):
        name = "None"

    try:
        teacher = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-table-cell.lecturer-cell"
        )[1].text
    except (IndexError, NoSuchElementException):
        teacher = "None"

    try:
        semester = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-table-cell.semester-cell"
        )[1].text
    except (IndexError, NoSuchElementException):
        semester = "None"

    try:
        credits = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-sub-table-cell.td2-cell"
        )[0].text
    except (IndexError, NoSuchElementException, ValueError):
        credits = "None"

    try:
        period = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-table-cell.period-cell"
        )[1].text
    except (IndexError, NoSuchElementException):
        period = "None"

    try:
        plan = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-card-body-pre"
        )[0].text
    except (IndexError, NoSuchElementException):
        plan = "None"

    try:
        how_grading = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-card-body-pre"
        )[1].text
    except (IndexError, NoSuchElementException):
        how_grading = "None"

    caution = "None"
    try:
        elements = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-card-body-pre"
        )
        if len(elements) > 2:
            caution = elements[2].text
        elif len(elements) > 1:
            caution = elements[1].text
    except NoSuchElementException:
        caution = "None"

    try:
        code = driver.find_elements(
            By.CSS_SELECTOR, ".catalog-page-detail-table-cell.code-cell"
        )[1].text
    except (IndexError, NoSuchElementException):
        code = "None"

    class_attributes = ClassAttributesScraping(
        name=name,
        teacher=teacher,
        semester=semester,
        credits=credits,
        period=period,
        plan=plan,
        how_grading=how_grading,
        caution=caution,
        code=code,
    )

    return class_attributes


# typesだとpythonの標準ライブラリと名前が被るのでtypeに変更
urls = get_urls()

driver = webdriver.Chrome()

"""
https://catalog.he.u-tokyo.ac.jp/result?q=&type=ug&faculty_id=3&facet=%7B%22semester_codes%22%3A%5B%22S1%22%2C%22S2%22%5D%7D&page=1
などから、授業の情報をスクレイピングする.

必要な授業情報のurlをpage parameter付きのurlを取得し、ループして保存する
"""

class_info = []

try:
    for page in range(1, 38):
        # ここのurlを必要なurlに変更する
        base_url = urls.engineering
        custom_url = base_url + str(page)
        driver.get(custom_url)
        detail_buttons = driver.find_elements(
            By.CLASS_NAME, "catalog-search-result-card-header-detail-link"
        )
        num_buttons = len(detail_buttons)

        for i in range(num_buttons):
            detail_buttons = driver.find_elements(
                By.CLASS_NAME, "catalog-search-result-card-header-detail-link"
            )
            detail_button = detail_buttons[i]

            detail_button.click()

            class_attribute = fetch_class_attributes(driver)

            class_info.append(class_attribute.dict())
            driver.back()
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()

# ここでclass_infoを保存する
with open("./data/工学部Sセメスター.json", "w", encoding="utf-8") as f:
    json.dump(class_info, f, ensure_ascii=False, indent=2)
