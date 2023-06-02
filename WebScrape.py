from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = 'https://www.etsy.com/ca/search?q=kimi%20no%20na%20wa&ref=auto-1&as_prefix=kimi%20no%20na%20wa'
path = 'F:/ChromeDriver/chromedriver_win32'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.implicitly_wait(20)
driver.get(website)

container = driver.find_elements(by='xpath',value='//ol[@class="wt-grid wt-grid--block wt-pl-xs-0 tab-reorder-container"]')

# /li/div/div/a/div/h3

titles = []
prices = []
numOfRatings = []

for i in container:
    title = driver.find_element(by='xpath', value='./li/div/div/a/div/h3').text
    price = driver.find_element(by='xpath', value='./li/div/div/a/div/div/p/span').text
    numOfRating = driver.find_element(by='xpath', value='./li/div/div/a/div/div//span/span[2]').text

    titles.append(title)
    prices.append(price)
    numOfRatings.append(numOfRating)

dict_etsy = {
    'titles': titles,
    'prices': prices,
    'numOfRatings': numOfRatings
}

pd.DataFrame(dict_etsy).to_csv('second_scrape.csv')

driver.quit()

# SAME ISSUES ON ETSY FOR SOME REASON
# selenium.common.exceptions.NoSuchElementException:...

# From my understanding, it is possible to web scrape etsy
# but for some reason I am getting this error.

# Possible Reasons:
# The html changes when the browser gets wider
# Etsy prevents any sort of web scraping
#
