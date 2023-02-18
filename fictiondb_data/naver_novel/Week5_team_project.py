from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from urllib.error import HTTPError
from urllib.error import URLError
from time import sleep
from selenium import webdriver
company_list = []
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path='C:/chromedriver_win32/chromedriver.exe')
driver.get('https://www.jobplanet.co.kr/users/sign_in?_nav=gb')
driver.implicitly_wait(3)
#	id,	비밀번호 전달
#	<input>의 이름이 id를 검색
driver.find_element_by_id('user_email').send_keys('gksfka12@knu.ac.kr')
driver.find_element_by_id('user_password').send_keys('hanlim0691')
driver.find_element_by_xpath('//*[@id="signInSignInCon"]/div[2]/div/section[3]/fieldset/button').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="JobPostingApp"]/div[3]/div[2]/div/button').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/nav/ul/li[1]/a').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="top5Companies"]/section[1]/div/p/a').click()
company_name_list = []
company_salary_list = []
company_location_list = []
company_score_list = []
for j in range(1, 101):
    driver.implicitly_wait(3)
    driver.get('https://www.jobplanet.co.kr/companies?industry_id=700&sort_by=review_survey_total_avg_cache&page={}'.format(j))  
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    company_name = soup.select('section.company > div.ty3_wrap> div.content_wrap > dl.content_col2_3.cominfo > dt.us_titb_l3 > a')
    company_salary = soup.select('section.company > div.ty3_wrap> div.content_wrap > dl.content_col2_4 > dd > a.us_stxt_1 > strong.notranslate')
    company_location = soup.select('section.company > div.ty3_wrap> div.content_wrap > dl.content_col2_3.cominfo > dd> span.us_stxt_1')
    company_score = soup.select('div.section_group > section.company > div > div > dl.content_col2_4 > dd.gf_row > span')

    driver.implicitly_wait(3)
    print(company_score)
    for i in company_name:
        company_name_list.append(i.text)
        print(i.text)
    for j in company_salary:
        company_salary_list.append(j.text)
        print(j.text)
    for z in company_location:
        company_location_list.append(z.text)
        print(z.text)  
    for u in company_score:
        company_score_list.append(u.text)
        print(u.text)        
    driver.implicitly_wait(3)

company_location_list= company_location_list[1::2]

x = {'기업이름':company_name_list, '기업지역': company_location_list, '기업연봉': company_salary_list, '기업평점': company_score_list}
rank = pd.DataFrame(x)
print(rank)
rank.to_csv('rank.csv',	encoding='utf-8', mode='w', index=True)