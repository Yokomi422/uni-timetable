import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from type import ClassAttributes, get_urls


def fetch_class_attributes(driver: WebDriver) -> ClassAttributes:
    name = driver.find_element(By.CSS_SELECTOR, "h1.color-ug").text
    teacher = driver.find_elements(
        By.CSS_SELECTOR, ".catalog-page-detail-table-cell.lecturer-cell"
    )[1].text
    semester = driver.find_elements(
        By.CSS_SELECTOR, ".catalog-page-detail-table-cell.semester-cell"
    )[1].text
    credits = int(
        driver.find_element(
            By.CSS_SELECTOR, ".catalog-page-detail-sub-table-cell.td2-cell"
        ).text
    )
    period = driver.find_elements(
        By.CSS_SELECTOR, ".catalog-page-detail-table-cell.period-cell"
    )[1].text
    plan = driver.find_element(
        By.CSS_SELECTOR, "div.catalog-page-detail-card-body-pre"
    ).text
    how_grading = driver.find_elements(
        By.CSS_SELECTOR, "div.catalog-page-detail-card-body-pre"
    )[1].text
    caution = driver.find_elements(
        By.CSS_SELECTOR, "div.catalog-page-detail-card-body-pre"
    )[2].text

    class_attributes = ClassAttributes(
        name=name,
        teacher=teacher,
        semester=semester,
        credits=credits,
        period=period,
        plan=plan,
        how_grading=how_grading,
        caution=caution,
    )

    return class_attributes


# typesだとpythonの標準ライブラリと名前が被るのでtypeに変更
urls = get_urls()

driver = webdriver.Chrome()

"""
https://catalog.he.u-tokyo.ac.jp/result?q=&type=ug&faculty_id=3&facet=%7B%22semester_codes%22%3A%5B%22S1%22%2C%22S2%22%5D%7D&page=1
などから、授業の情報をスクレイピングする
"""
try:
    for page in range(1, 38):
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

            print(class_attribute.dict())

            driver.back()
except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
