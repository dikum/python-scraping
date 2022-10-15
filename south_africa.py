from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




national_covid_report_website = 'https://www.nicd.ac.za/diseases-a-z-index/disease-index-covid-19/surveillance-reports/national-covid-19-daily-report/'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.get(national_covid_report_website)

total_tests_conducted = []
confirmed_cases = []
past_24hrs_tests = []
past_24hrs_cases = []

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@loading='lazy']")))
total_tests_conducted.append(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[@id='chtTests']"))).text)
confirmed_cases.append(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[@id='chtCases']"))).text)
past_24hrs_tests.append(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[@id='chtTestsPrevious']"))).text)
past_24hrs_cases.append(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//h2[@id='chtCasesPrevious']"))).text)

driver.quit()

df = pd.DataFrame({'Total Tests Conducted': total_tests_conducted, 'Confirmed Cases' : confirmed_cases, 'Past 24 Hrs Tests': past_24hrs_tests, 'Past 24 Hrs Cases':past_24hrs_cases})
df.to_csv('downloads/sa_covid.csv', index=False)
