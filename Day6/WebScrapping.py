# Chapter 11: Web Scraping

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import json
import time

# 1. Fetching Web Pages with requests
response = requests.get('https://example.com')
if response.status_code == 200:
    print(response.text[:500])  # Print first 500 characters of the HTML

# 2. Parsing HTML with Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find('title')  # Find the <title> tag
print(f"Title: {title.text}")

# Using CSS selectors
links = soup.select('a')  # Select all <a> tags
for link in links[:5]:  # Limit to first 5 links
    print(link.get('href'))

# 3. Automating with Selenium
driver = webdriver.Chrome()  # Requires chromedriver setup
driver.get('https://example.com')

search_box = driver.find_element('name', 'q')  # Find search box by name
search_box.send_keys('Python')
search_box.submit()

time.sleep(3)  # Wait for results to load
driver.quit()

# 4. Saving Scraped Data
# Save to a CSV file
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Header1', 'Header2'])
    writer.writerow(['Value1', 'Value2'])

# Save to a JSON file
scraped_data = {'title': title.text, 'links': [link.get('href') for link in links[:5]]}
with open('data.json', 'w') as jsonfile:
    json.dump(scraped_data, jsonfile)
