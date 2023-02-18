from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from selenium import webdriver
import time

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
search = driver.find_element_by_xpath('//*[@id="search_bar_search_query"]')
# search_list= ['빅데이터']
driver.implicitly_wait(3)
search.send_keys('빅데이터')
search.submit()
driver.find_element_by_xpath('//*[@id="mainContents"]/div[2]/div[1]/a').click()
driver.implicitly_wait(3)
requirement = []
recruit_name = []
company_name = []
company_location = []
company_score = []

for i in range(1,11):
    try:
        driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/section/div[1]/div[2]/ul/li[{}]/a/p[1]'.format(i)).click()
    except:
        continue
    driver.implicitly_wait(3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    requirement_str=[]
    
    x = soup.select_one('div.lft h1.ttl')
    recruit_name.append(x.text)
    driver.implicitly_wait(3)
    y = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_wrap_new.company_job_details > div > div.wrap > div > div > div.block_job_posting > section > div:nth-child(4) > p')
    driver.implicitly_wait(3)
    z = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.company_name > a')
    for i in y:
        requirement_str.append(i.text)
    requirement_str
    requirement.append(''.join(requirement_str))
    z = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.company_name > a')
    company_name.append(z.text)
    print(requirement)
    u = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.job_location > span')
    company_location.append(u.text)
    o = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.recruitment-score')
    company_score.append(o.text)
    driver.implicitly_wait(3)
    

for i in range(2,6):
    if i == 2: 
        driver.execute_script("window.scrollTo(0,4000)")
    else: 
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.implicitly_wait(3)
    driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/section/div[1]/div[3]/button[{}]'.format(i)).click()
    driver.implicitly_wait(3)
    for i in range(1,11):
        try:
            driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/section/div[1]/div[2]/ul/li[{}]/a/p[1]'.format(i)).click()
            driver.implicitly_wait(3)
        except:
            continue
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        requirement_str=[]    
        x = soup.select_one('div.lft h1.ttl')
        recruit_name.append(x.text)
        driver.implicitly_wait(3)
        y = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_wrap_new.company_job_details > div > div.wrap > div > div > div.block_job_posting > section > div:nth-child(4) > p')
        driver.implicitly_wait(3)
        for i in y:
            requirement_str.append(i.text)
        
        requirement_str
        requirement.append(''.join(requirement_str))
        z = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.company_name > a')
        company_name.append(z.text)
        print(requirement)
        u = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.job_location > span')
        company_location.append(u.text)
        o = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.recruitment-score')
        company_score.append(o.text)
        driver.implicitly_wait(3)
   
print(company_name)        
print(requirement)
print(company_location)
print(recruit_name)
print(company_score)
len(requirement)
len(company_name)
len(company_score)
while True:
    import time
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.implicitly_wait(3)
    try:    
        driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/section/div[1]/div[3]/button[5]').click()
        driver.implicitly_wait(3)  
    except:
        break
    time.sleep(0.4)
    driver.implicitly_wait(3) 
    for i in range(1,11):
        try:
            driver.find_element_by_xpath('//*[@id="job_search_app"]/div/div[2]/section/div[1]/div[2]/ul/li[{}]/a/p[1]'.format(i)).click()
            driver.implicitly_wait(3)
        except:
            continue
        time.sleep(0.4) 
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        requirement_str=[]    
        x = soup.select_one('div.lft h1.ttl')
        recruit_name.append(x.text)
        driver.implicitly_wait(3)
        y = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_wrap_new.company_job_details > div > div.wrap > div > div > div.block_job_posting > section > div:nth-child(4) > p')
        driver.implicitly_wait(3)
        for i in y:
            requirement_str.append(i.text)
        requirement_str
        driver.implicitly_wait(3)
        z = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.company_name > a')
        company_name.append(z.text)
        requirement.append(''.join(requirement_str))
        print(requirement)
        u = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.job_location > span')
        company_location.append(u.text)
        o = soup.select_one('#job_search_app > div > div.job_search_content > section > div.job_search_detail > div > div > div > div.job_apply_section > div > div > div.lft > div > div > div > span.recruitment-score')
        company_score.append(o.text)
        driver.implicitly_wait(3)
        time.sleep(0.4)

ready_to_dataframe = {'회사이름':company_name, '채용공고':recruit_name, '회사평점':company_score,'회사지역':company_location, '자격요건':requirement}
df_bigdata_recruit = pd.DataFrame(ready_to_dataframe)
df_bigdata_recruit.to_csv('bigdata_recruit.csv', encoding='utf-8', mode='w', index=True)
