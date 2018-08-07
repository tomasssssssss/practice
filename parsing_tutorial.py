from selenium import webdriver
import sqlite3

connection = sqlite3.connect('naver_news.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS news")
cursor.execute('''
CREATE TABLE news (
    title VARCHAR(100),
    contents VARCHAR(10000))
''')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--window-size = 1920x1080')
options.add_argument('--disable-gpu')

phantom_path = r'C:\Users\13ZD\Desktop\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin/phantomjs'
driver = webdriver.PhantomJS(executable_path=phantom_path)

get_url = r'https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=226'
driver.get(get_url)
title_xpath = r'//*[@id="main_content"]/div[2]/ul[*]/li[*]/dl/dt[2]/a'
title_element_list = driver.find_elements_by_xpath(title_xpath)

title_url_list = list()
title_list = list()
article_text_list = list()

for title_element in title_element_list :
    title_url = title_element.get_attribute('href')
    title_list.append(title_element.text)
    title_url_list.append(title_url)

for title_url in title_url_list :
    driver.get(title_url)
    article_text = driver.find_element_by_id('articleBodyContents').text
    article_text_list.append(article_text)

title = ','.join(title_list)
article = ','.join(article_text_list)

value_set = (title, article)
cursor.execute('INSERT INTO news VALUES(?,?)', value_set)