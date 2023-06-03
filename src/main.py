import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
option.add_argument('--disable-gpu')
option.add_argument('--lang=en')
service = Service('C:\\repos\\PythonVenv\\scraping\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=option)
driver.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(driver.page_source, 'html.parser')

totalInfo = []

links = soup.select("table tbody tr td.titleColumn a")
first10 = links[:10]
for anchor in first10:
    print(anchor.text)
    print(anchor['href'])
    driver.get('https://www.imdb.com/' + anchor['href'])
    infolist = driver.find_element(By.CLASS_NAME, 'ipc-inline-list')[0]
    # informations = infolist.find_element(By.CSS_SELECTOR, "[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
    # scrapedInfo = {
    #     "title": anchor.text,
    #     "year": informations[0].text,
    #     "duration": informations[2].text,
    # } # Save all the scraped information in a dictionary
    # totalInfo.append(scrapedInfo)

print(totalInfo)

