#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 16:37:36 2022

@author: Zilin Luo
"""


# %%%% topic: Data Scrapping -  basic
import datetime
import pandas as pd
import re
import time
import numpy as np

# libraries to crawl websites
from bs4          import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

# from pynput.mouse import Button, Controller

path_to_driver = "/Users/rosalind/Downloads/chromedriver 3"
driver = webdriver.Chrome(executable_path=
                          path_to_driver)
driver.get("http://www.google.com")
print(driver.title)

## %% 
#links_to_scrape = 'https://www.tripadvisor.com/Attraction_Review-g57302-d107087-Reviews-Killington_Resort-Killington_Vermont.html'
                   
#driver.get(links_to_scrape)
#time.sleep(1)

links_to_scrape = ['https://www.tripadvisor.com/Attraction_Review-g57302-d107087-Reviews-Killington_Resort-Killington_Vermont.html',
                   'https://www.tripadvisor.com/Attraction_Review-g57415-d106650-Reviews-Stowe_Mountain_Resort-Stowe_Vermont.html',
                   'https://www.tripadvisor.com/Attraction_Review-g46140-d105903-Reviews-Loon_Mountain_Resort-Lincoln_New_Hampshire.html']
l               = 2
one_link        = links_to_scrape[l]
driver.get(one_link)
time.sleep(2)

#%%%%%
reviews_killington = []
reviews_stowe = []
reviews_loon = []
r = 0
while True:    
    reviews = driver.find_elements(By.XPATH, "//div[@class='_c']")   
    for r in range(len(reviews)):
        review = {}       
        soup = BeautifulSoup(reviews[r].get_attribute('innerHTML'))
        try:
            rating_star =soup.find('svg', attrs={'class':'UctUV d H0'})['aria-label'][0]
        except:
            rating_star = ""
        review['rating_star']= rating_star
        try:
            review_title = soup.find('span', attrs={'class':'yCeTE'}).text
        except:
            review_title = ""
        try:
            text = soup.find('span', attrs={'class':'yCeTE'}).find_next("span").text
        except:
            text = ""
        review['text'] = review_title+". "+text
        try:    
            date = soup.find('div', attrs={'class':'RpeCd'}).text[0:8]
        except:
            date =""
        review['date'] = date
        reviews_loon.append(review)
        time.sleep(1)
    try:
        driver.find_element(By.XPATH,"//div[@class='xkSty']").click()
    except:
        break
    time.sleep(3)
           
df_k = pd.DataFrame(reviews_killington)
df_k["ski_resort"] = "K"
df_k.to_csv("/Users/rosalind/Desktop/mkt analytics/scraping/final project/reviews_k.csv")  
df_s = pd.DataFrame(reviews_stowe)
df_s["ski_resort"] = "S"
df_s.to_csv("/Users/rosalind/Desktop/mkt analytics/scraping/final project/reviews_s.csv")  
df_l = pd.DataFrame(reviews_loon)
df_l["ski_resort"] = "L"
df_l.to_csv("/Users/rosalind/Desktop/mkt analytics/scraping/final project/reviews_l.csv")  
df = pd.concat([df_k, df_s, df_l])
df.to_csv("/Users/rosalind/Desktop/mkt analytics/scraping/final project/reviews.csv") 
#%%%%%
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer










       