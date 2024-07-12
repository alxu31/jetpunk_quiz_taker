# Required modules, need to pip install
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from driverpath import driverPath
#? imports private file with driver path, use your own
#? driver_path = 'C:\\Users\\_____\\_____\\_____\\chromedriver.exe'

# Scrape page for answers
def scrape(url) -> list:
    service = Service(driverPath)
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    # Let page load
    time.sleep(2)
    
    try:
        # Click start and give up buttons
        start = driver.find_element(By.CSS_SELECTOR, '#start-button')
        start.click()
        time.sleep(1)
        giveUp = driver.find_element(By.CSS_SELECTOR, '.give-up')
        giveUp.click()
        time.sleep(1)
    except Exception as e:
        print("Could not find or click the start and give up buttons:", e)

    # Answer elements
    ansElems = driver.find_elements(By.CSS_SELECTOR, '.answer-display')

    # Replace newline with space
    answers = [element.text.replace('\n', ' ') for element in ansElems]

    driver.quit()

    return answers

#* URL of the JetPunk quiz e.g. https://www.jetpunk.com/quizzes/how-many-countries-can-you-name
url = input('Url: ')

answers = scrape(url)

#? Testing
if __name__ == '__main__':
    print(answers)