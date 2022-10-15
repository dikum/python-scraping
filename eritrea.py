from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re
import pandas as pd


website = 'https://shabait.com/2022/05/09/announcement-from-the-ministry-of-health-470/'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(website)

match = driver.find_element(By.XPATH, "//span[@class='post-title']")

if 'Announcement from the Ministry of Health' in match.text:
    content = driver.find_element(By.XPATH, "//div[contains(@class, 'single-post-content')]")
    paragraph2 = content.find_element(By.XPATH, './p[2]').text.replace(",", "")
    paragraph3 = content.find_element(By.XPATH, './p[3]').text.replace(",", "")

    cummulative_cases = re.findall('[0-9]+', paragraph2)
    numbers = re.findall('[0-9]+', paragraph3)
    cummulative_recovered = numbers[0]
    cummulative_deaths = numbers[1]

    driver.close()


    df = pd.DataFrame({'Cummulative cases': cummulative_cases, 'Cummulative Recovered' : cummulative_recovered, 'Cummulative deaths': cummulative_deaths})
    df.to_csv('downloads/eritrea.csv', index=False)







