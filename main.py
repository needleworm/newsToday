from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from datetime import datetime as dt
import sys


id = sys.argv[1]
ps = sys.argv[2]


url = "https://www.tistory.com/auth/login"

opt = webdriver.ChromeOptions()
# opt.add_argument("headless")
# opt.add_argument("window-size=1920x1080")
# opt.add_argument("disable-gpu")
opt.add_argument("log-level=3")

driver = webdriver.Chrome("./chromedriver", chrome_options=opt)




def login(id, ps):
    driver.get(url)
    time.sleep(4)

    loginButton = driver.find_element(By.CLASS_NAME, "btn_login.link_kakao_id")
    loginButton.click()

    idField = driver.find_element(By.ID, "input-loginKey")
    idField.send_keys(id)

    psField = driver.find_element(By.ID, "input-password")
    psField.send_keys(ps)
    psField.send_keys(Keys.RETURN)

    time.sleep(3)


def write_article(title, contents):
    driver.get("https://bhban.tistory.com/manage/newpost/?type=post")
    time.sleep(1)

    try:
        result = driver.switch_to.alert
        result.dismiss()
    except:
        pass
    time.sleep(1)

    category_button = driver.find_element(By.CLASS_NAME, "mce-txt")
    category_button.click()
    news = driver.find_element(By.ID, "category-item-1056082")
    news.click()

    title_section = driver.find_element(By.ID, "post-title-inp")
    title_section.send_keys(title)
    title_section.send_keys(Keys.TAB)

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    for cnt in contents:
        iframe.send_keys(cnt)
        iframe.send_keys(Keys.RETURN)
        iframe.send_keys("\n\n\n")

    time.sleep(10)

    publish_layer_button = driver.find_element(By.ID, "publish-layer-btn")
    publish_layer_button.click()
    time.sleep(2)

    #noneButton = driver.find_element(By.ID, "open0")
    #noneButton.click()

    try:
        publish_button = driver.find_element(By.ID, "publish-btn")
        publish_button.click()
    except:
        time.sleep(1)
        publish_button = driver.find_element(By.ID, "publish-btn")
        publish_button.click()

    while "https://bhban.tistory.com/manage/posts/" not in driver.current_url:
        time.sleep(1)

    print(title + " was Written")


def get_newses():
    ret = []

    today = str(dt.now().date()).split("-")
    today = "[" + today[0] + "년 " + today[1] + "월 " + today[2] + "일]"

    # 헤드라인들
    driver.get("https://news.google.com/topstories")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 뉴스 헤드라인", headlines))

    # 대한민국 소식
    driver.get("https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFp4WkRNU0FtdHZLQUFQAQ")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 대한민국 뉴스", headlines))

    # 세계 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtdHZHZ0pMVWlnQVAB")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 세계 뉴스", headlines))

    # 안동 소식
    driver.get("https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections"
               "/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNRE4yT1"
               "RSZmVnc0tDUzl0THpBemRqazBYeWdBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNR"
               "E4yT1RSZktBQVABUAE?hl=ko&gl=KR&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 경북 안동시 뉴스", headlines))

    # 비즈니스 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR"
               "&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 경제, 사업분야 뉴스", headlines))

    # 과학기술 소식
    driver.get("https://news.google.com/topics/CAAqKAgKIiJDQkFTRXdvSkwyMHZNR1ptZHpWbUVnSnJieG9DUzFJb0FBUAE?hl=ko&gl"
               "=KR&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 과학기술 뉴스", headlines))

    # 엔터테인먼트 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR"
               "&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 엔터테인먼트 뉴스", headlines))

    # 연예 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtdHZHZ0pMVWlnQVAB/sections"
               "/CAQiRkNCQVNMZ29JTDIwdk1ESnFhblFTQW10dkdnSkxVaUlPQ0FRYUNnb0lMMjB2TURGeVpub3FDaElJTDIwdk1ERnlabm9"
               "vQUEqKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURKcWFuUVNBbXR2R2dKTFVpZ0FQAVAB?hl=ko&gl=KR&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 연예 뉴스", headlines))

    # 스포츠 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtdHZHZ0pMVWlnQVAB?hl=ko&gl=KR"
               "&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 스포츠 뉴스", headlines))

    # KBO 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtdHZHZ0pMVWlnQVAB/sections"
               "/CAQiRENCQVNMUW9JTDIwdk1EWnVkR29TQW10dkdnSkxVaUlRQ0FRYURBb0tMMjB2TUdOb05GOWtOQ29IQ2dVU0EwdENUeWd"
               "BKioIAComCAoiIENCQVNFZ29JTDIwdk1EWnVkR29TQW10dkdnSkxVaWdBUAFQAQ?hl=ko&gl=KR&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 KBO 야구 뉴스", headlines))

    # KBL 소식
    driver.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtdHZHZ0pMVWlnQVAB/sections"
               "/CAQiQ0NCQVNMQW9JTDIwdk1EWnVkR29TQW10dkdnSkxVaUlQQ0FRYUN3b0pMMjB2TURWeGVYcHVLZ2NLQlJJRFMwSk1LQUE"
               "qKggAKiYICiIgQ0JBU0Vnb0lMMjB2TURadWRHb1NBbXR2R2dKTFVpZ0FQAVAB?hl=ko&gl=KR&ceid=KR%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 KBL 농구 뉴스", headlines))

    # 건강 소식
    driver.get("https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtdHZLQUFQAQ?hl=ko&gl=KR&ceid=KR"
               "%3Ako")
    time.sleep(4)
    articles = driver.find_elements(By.TAG_NAME, "article")
    headlines = []

    for article in articles:
        urls = article.find_element(By.TAG_NAME, "a")
        href = urls.get_attribute("href")
        headlines.append(href)

    ret.append((today + " 오늘의 건강, 의햑 뉴스", headlines))

    return ret


newses = get_newses()
for el in newses:
    title, contents = el
    write_article(title, contents)

