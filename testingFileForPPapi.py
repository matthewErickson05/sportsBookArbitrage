from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import undetected_chromedriver as uc
import json
import requests
from bs4 import BeautifulSoup

PATH = "C:\Program Files (x64)\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://api.prizepicks.com/projections")
#This is a good website that brings up the JSON format for all the projections on prizepicks
#Problem: api gives player, team, and league information in id format, need names

time.sleep(2)


json_data = driver.find_element("tag name", 'pre').text

response = json.loads(json_data)

#print(response)
driver.quit()

players = {}
for d in response["included"]:
    if d['type'] == 'new_player' :
        players[d["id"]] = d["attributes"]


#Shesterkin id is 218676
# for player in players.values() :
#     print(player['name'])

data = []
for d in response['data']:
    if d['type'] == 'projection' :
        # print(players[d['relationships']['new_player']['data']['id']]['name'])
        data.append({
        **d['attributes'],
        'name': players[d['relationships']['new_player']['data']['id']]['name']
        })
        print(players[d['relationships']['new_player']['data']['id']]['name'] + " " + str(d['attributes']['line_score']) + " " + d["attributes"]['stat_type'])


df = pd.DataFrame(data)
print(df)