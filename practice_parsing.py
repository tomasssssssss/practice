from selenium import webdriver

title_element_list = list()
title_url_list = list()

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--window-size = 1920x1080')

chrome_path = r'C:\Users\13ZD\Desktop\chromedriver_win32/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)

options.add_argument('--disable-gpu')
get_url = r'http://www.megabox.co.kr/?menuId=movie'
driver.get(get_url)


for i in range(2,5) :
    content = driver.find_element_by_xpath(r'//*[@id="movieList"]/li[{}]/div[2]/div[2]/h3/a'.format(i))
    content.click()

    title_xpath = r'//*[@id="movieDetail"]/div[1]/div[2]/div[1]/h2/span'
    title = driver.find_element_by_xpath(title_xpath)
    print('제목 : ', title.text)

    actor_xpath = r'//*[@id="movieDetail"]/div[1]/div[2]/div[2]/ul/li[4]'
    actor = driver.find_element_by_xpath(actor_xpath)
    print(actor.text)

    genre_xpath = r'//*[@id="movieDetail"]/div[1]/div[2]/div[2]/ul/li[5]'
    genre = driver.find_element_by_xpath(genre_xpath)
    print(genre.text)

    content_xpath = r'//*[@id="movieDetail"]/div[2]/div/text()[*]'
    content = driver.find_element_by_xpath(content_xpath)
    print('내용 : ', content.text)

    btn = driver.find_element_by_xpath(r'//*[@id="movie_detail"]/div/div/button').click()