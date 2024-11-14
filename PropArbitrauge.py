from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import undetected_chromedriver as uc
import json

PATH = "C:\Program Files (x64)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://api.prizepicks.com/projections")
#This is a good website that brings up the JSON format for all the projections on prizepicks
#Problem: api gives player, team, and league information in id format, need names



time.sleep(2)

#driver.find_element(By.CLASS_NAME, "close").click()



driver.find_element("tag name", 'pre').text

time.sleep(2)

stat_container = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "stat-container")))

stat_elements = driver.find_elements(By.CSS_SELECTOR, "div.stat")

nbaPlayers = []

for stat in stat_elements:
    stat.click()

    projections = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".projection")))

    for projection in projections : 
        names = projection.find_element(By.XPATH, './/div[@class="name"]').text
        points= projection.find_element(By.XPATH, './/div[@class="presale-score"]').get_attribute('innerHTML')
        text = projection.find_element(By.XPATH, './/div[@class="text"]').text
        print(names, points, text)

        players = {
            'Name': names,
            'Prop':points, 'Line':text
            }

        nbaPlayers.append(players)
   

df = pd.DataFrame(nbaPlayers)
print(df)

driver.quit()