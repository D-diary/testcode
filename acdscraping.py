from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient
import requests

client = MongoClient('localhost', 27017)

db = client.academy
driver = webdriver.Chrome()
# url 설정
url = "https://map.naver.com/v5"
# 검색어 설정
findAcademy = ["서울 컴퓨터학원", "인천 컴퓨터학원", "경기도 컴퓨터학원"]
driver.get(url)
time.sleep(5)
for aca in findAcademy:
    elem = driver.find_element_by_css_selector(
      "#container > shrinkable-layout > div > app-base > search-input-box > div > div > div > input")
    # 검색어 입력
    print(aca, "크롤링 시작...")
    elem.clear()
    elem.send_keys(aca)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)

    searchiframe = driver.find_element_by_id("searchIframe")
    driver.switch_to.frame(searchiframe)

    pagebar = driver.find_element_by_class_name("_34lTS").text
    print(pagebar)

    page = 1

    while pagebar != "다음페이지":
        # iframe 스크롤 내리기 ( 무식한 방법 ) / iframe 내부의 요소를 지정하여 그곳까지 이동. 자동으로 끝까지 내리게 하고싶은데.. 이 방법도 기능적으로 문제는 없음.
        actions = ActionChains(driver)

        scroll1 = driver.find_element_by_css_selector("#_pcmap_list_scroll_container > ul > li:nth-child(10)")
        actions.move_to_element(scroll1).perform()

        scroll2 = driver.find_element_by_css_selector("#_pcmap_list_scroll_container > ul > li:nth-child(20)")
        actions.move_to_element(scroll2).perform()

        scroll3 = driver.find_element_by_css_selector("#_pcmap_list_scroll_container > ul > li:nth-child(30)")
        actions.move_to_element(scroll3).perform()

        scroll4 = driver.find_element_by_css_selector("#_pcmap_list_scroll_container > ul > li:nth-child(40)")
        actions.move_to_element(scroll4).perform()

driver.quit()