from bs4 import BeautifulSoup as soup 
from urllib.request import Request, urlopen as req
import re
from pandas import DataFrame
import pandas
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from time import sleep 
import requests

from bs4 import BeautifulSoup as Soup
import hashlib 

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://dt.data1688.com/login")

print("Title of the page :",  driver.title)

productDescription = []
descriptions = [[]]


usernameElement = driver.find_element_by_id('userName')
usernameElement.send_keys('yixunhui')
print("username",type(usernameElement))


passwordElement = driver.find_element_by_id('password')
passwordElement.send_keys('h888888')

passwordElement.send_keys(Keys.RETURN)
print("password", type(passwordElement))

try:
    searchInput = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div[1]/div[2]/div/div/ul/li/div/span[1]/span/span[1]/input'))
    )
    searchInput.send_keys('L')
    searchInput.send_keys(Keys.RETURN)
    

    sleep(30)
    rows = driver.find_elements_by_class_name('overseas-table-column-goodsDesc')
    print("length",len(rows))
    i =1
    while i < 22:
        if i == 0:
            continue

        
        rows[i].find_elements_by_tag_name('a')[0].click()
        sleep(8)
        page = soup(driver.page_source)
        u = 0
        tables  = page.findAll('table')
        while u < 6: 
            table = tables[u]
            values = table.findChildren(['td'])
            
            print('len of td',len(values))
            for value in values:
                print(value.text)
                productDescription.append(value.text)
            u+=1
        print(len(productDescription))
        descriptions.append(productDescription)
        with open('data.csv', 'a') as fd: 
            fd.write()
        
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        sleep(2)
        i+=1
except Exception as e:
    print('exception')
    print(e.code)