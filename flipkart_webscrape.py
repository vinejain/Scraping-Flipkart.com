# -*- coding: utf-8 -*-
# Flipkart scraping
# Source: https://www.edureka.co/blog/web-scraping-with-python/
"""
Created on Sat Feb  1 17:14:44 2020

@author: Vineet PC
"""

from selenium import webdriver
#importing BeautifulSoup latest version bs4
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Chrome("D:/D Downloads/chromedriver_win32/chromedriver.exe")
products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating=a.find('div', attrs={'class':'hGSR34'})
    ratingsCount=a.find('div', attrs={'class':'_38sUEc'})
    reviewsCount=a.find('div', attrs={'class':'_1VpSqZ'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)
    ratingsCount.append(ratingsCount.text)
    reviewsCount.append(reviewsCount.text)
    
df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
