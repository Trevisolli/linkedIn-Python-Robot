from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import dotenv
import os 
import time

dotenv.load_dotenv(dotenv.find_dotenv())
username = os.getenv("username")
lastname = os.getenv("lastname")
mail = os.getenv("mail")
domain = os.getenv("domain")
passwd = os.getenv("password")
login = (username+"."+lastname+"@"+mail+"."+domain)

options = webdriver.ChromeOptions()
options.add_argument("--disable-logging")
options.add_argument("--log-level-3")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
service = Service(ChromeDriverManager().install())

#Login
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.linkedin.com/login")
id_login = "username"
id_passwd = "password"
input_email = driver.find_element("id", id_login)
input_email.send_keys(login)
input_passwd = driver.find_element("id", id_passwd)
input_passwd.send_keys(passwd)
time.sleep(1)
button_login = driver.find_element("xpath", '//*[@id="organic-div"]/form/div[3]/button')
time.sleep(1)
button_login.submit()
time.sleep(3)

#Data Engineer Job search
search_job = driver.find_element("xpath", "//input[@aria-label='Search']")
search_job.click()
time.sleep(3)
search_job.send_keys("Engenheiro de Dados")
time.sleep(3)
search_job.send_keys(Keys.RETURN)
time.sleep(5)

#Only on Jobs
only_job = driver.find_element("xpath", '//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
time.sleep(3)
only_job.click()
time.sleep(10)


jobs_list= driver.find_elements(By.CSS_SELECTOR, '.jobs-search-results__list-item')
    
for job in jobs_list:
    job_title = job.find_element(By.XPATH,'.//*[@class="disabled ember-view job-card-container__link job-card-list__title"]')                                                        
    job_company = job.find_element(By.XPATH,'.//*[@class="app-aware-link "]') 
    job_place = job.find_element(By.XPATH,'.//*[@class="job-card-container__metadata-item "]')
    title = job_title.text if job_title else None
    company = job_company.text if job_company else None 
    place = job_place.text if job_place else None 
    print(title, " - ",  company, " - ",  place)        
    driver.execute_script("arguments[0].scrollIntoView();", job)



time.sleep(3)

driver.close()